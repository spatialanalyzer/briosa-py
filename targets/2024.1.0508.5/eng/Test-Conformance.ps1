[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$ArtifactPath,

    [string]$LockPath = "conformance.lock.json",

    [string]$EvidencePath,

    [string]$FixturePath,

    [hashtable]$ClientPackage,

    [switch]$ExpectIncompatible,

    [ValidateRange(1, 1000)][int]$RequiredContractMajor = 3,

    # Longer than the 180 s an omitted startup budget can reach against a
    # conformance server, which sets a 30 s worker start bound.
    [ValidateRange(5, 600)][int]$FixtureTimeoutSeconds = 240,

    [string]$PythonExecutable = "python"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not $IsWindows -or -not [Environment]::Is64BitProcess) {
    throw "The shared client conformance suite requires 64-bit Windows."
}

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$resolvedArtifact = [IO.Path]::GetFullPath($ArtifactPath, $repositoryRoot)
$lock = Get-Content -LiteralPath ([IO.Path]::GetFullPath($LockPath, $repositoryRoot)) -Raw |
    ConvertFrom-Json
$temporaryBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$temporaryRoot = Join-Path $temporaryBase "briosa-py-conformance-$([Guid]::NewGuid().ToString('N'))"

if (-not (Test-Path -LiteralPath $resolvedArtifact -PathType Leaf)) {
    throw "The conformance artifact does not exist."
}
$artifactHash = (Get-FileHash -LiteralPath $resolvedArtifact -Algorithm SHA256).Hash.ToLowerInvariant()
if ($artifactHash -ne $lock.artifact.sha256) {
    throw "The conformance artifact SHA-256 does not match conformance.lock.json."
}
$externalChecksum = (Get-Content -LiteralPath "$resolvedArtifact.sha256" -Raw).Trim()
if ($externalChecksum -ne "$artifactHash  $([IO.Path]::GetFileName($resolvedArtifact))") {
    throw "The adjacent conformance artifact checksum is invalid."
}

[IO.Directory]::CreateDirectory($temporaryRoot) | Out-Null
# Portable conformance owns fake processes and must not launch a desktop monitor.
$previousDesktopMode = [Environment]::GetEnvironmentVariable("Briosa__Desktop__Mode")
$previousExpectation = [Environment]::GetEnvironmentVariable("BRIOSA_CONFORMANCE_EXPECT_INCOMPATIBLE")
$env:BRIOSA_CONFORMANCE_EXPECT_INCOMPATIBLE = $(if ($ExpectIncompatible) { '1' } else { '0' })
$selectedScenarios = $(if ($ExpectIncompatible) { @('control-plane-only') } else { @() })
$env:Briosa__Desktop__Mode = "Disabled"
try {
    Expand-Archive -LiteralPath $resolvedArtifact -DestinationPath $temporaryRoot
    $packageRoots = @(Get-ChildItem -LiteralPath $temporaryRoot -Directory)
    if ($packageRoots.Count -ne 1) {
        throw "The conformance artifact must contain exactly one root directory."
    }
    $packageRoot = $packageRoots[0].FullName
    $manifest = Get-Content -LiteralPath (Join-Path $packageRoot "manifest.json") -Raw |
        ConvertFrom-Json
    if ($manifest.artifactKind -ne "briosa_client_conformance" -or
        $manifest.artifactName -ne $lock.artifact.name -or
        $manifest.briosaVersion -ne $lock.artifact.briosa_version -or
        $manifest.sourceRevision -ne $lock.artifact.source_revision -or
        $manifest.spatialAnalyzerTarget -ne $lock.target.spatial_analyzer -or
        $manifest.scenarioContract -ne $lock.contract.id -or
        $manifest.scenarioContractSchemaVersion -ne $lock.contract.schema_version) {
        throw "The conformance artifact identity does not match conformance.lock.json."
    }

    $runner = Join-Path $packageRoot "runner\Invoke-BriosaClientConformance.ps1"
    $fixture = Join-Path $repositoryRoot "tools\client_conformance.py"
    if ($FixturePath) { $fixture = [IO.Path]::GetFullPath($FixturePath, $repositoryRoot) }
    $scenarios = Get-Content (Join-Path $packageRoot "contract/scenarios.json") -Raw | ConvertFrom-Json
    # Optional scenarios run only on request. Ask for the ones this fixture knows
    # when the packaged runner accepts -OptionalScenario (Server 0.10.1 and later)
    # and its contract lists them; the rejection path runs control-plane-only alone.
    $fixtureOptionalScenarios = @('large-result')
    $optionalScenarios = @()
    if (-not $ExpectIncompatible -and
        (Get-Command -Name $runner).Parameters.ContainsKey('OptionalScenario') -and
        $scenarios.PSObject.Properties.Name -contains 'optional_scenarios') {
        $optionalScenarios = @($scenarios.optional_scenarios |
            ForEach-Object { [string]$_.id } |
            Where-Object { $_ -in $fixtureOptionalScenarios })
    }
    $runnerArguments = @{
        Scenario = $selectedScenarios
        FixtureCommand = $PythonExecutable
        FixtureArguments = @($fixture)
    }
    if ($optionalScenarios.Count -gt 0) { $runnerArguments.OptionalScenario = $optionalScenarios }
    # Every runner from 0.9.2 accepts -FixtureTimeoutSeconds; record what was used.
    $fixtureTimeout = $null
    if ((Get-Command -Name $runner).Parameters.ContainsKey('FixtureTimeoutSeconds')) {
        $fixtureTimeout = $FixtureTimeoutSeconds
        $runnerArguments.FixtureTimeoutSeconds = $fixtureTimeout
    }
    & $runner @runnerArguments
    if (-not [string]::IsNullOrWhiteSpace($EvidencePath)) {
        $protocol = Get-Content (Join-Path $repositoryRoot "protocol.lock.json") -Raw | ConvertFrom-Json
        $clientRoot = (Split-Path (Split-Path $repositoryRoot -Parent) -Parent).Replace('\', '/')
        $clientRevision = [string](& git -c "safe.directory=$clientRoot" -C $clientRoot rev-parse HEAD)
        if ($LASTEXITCODE -ne 0) { throw "Cannot identify client source for evidence." }
        $dirty = @(& git -c "safe.directory=$clientRoot" -C $clientRoot status --porcelain).Count -ne 0
        if ($LASTEXITCODE -ne 0) { throw "Cannot identify client worktree state." }
        $report = [ordered]@{
            schemaVersion = 1
            generatedAt = [DateTimeOffset]::UtcNow.ToString("O")
            validationKind = $(if ($ExpectIncompatible) { "client-server-compatibility-rejection" } elseif ($ClientPackage) { "packaged-client-and-server-fake-sdk" } else { "packaged-server-fake-sdk" })
            expectedCompatibility = $(if ($ExpectIncompatible) { "rejected" } else { "accepted" })
            passed = $true
            licensedSpatialAnalyzer = $false
            client = @{
                repository = "https://github.com/spatialanalyzer/briosa-py"
                # A package run records the package tested; a source run, the project.
                version = $(if ($ClientPackage) { [string]$ClientPackage.version } else { ([regex]::Match((Get-Content (Join-Path $repositoryRoot "pyproject.toml") -Raw), '(?m)^version = "([^"]+)"')).Groups[1].Value })
                sourceRevision = $(if ($ClientPackage) { $ClientPackage.sourceRevision } else { $clientRevision })
                uncommittedChanges = $(if (-not $ClientPackage) { $dirty } else { $null })
                fixtureSourceRevision = $clientRevision
                fixtureUncommittedChanges = $dirty
                package = $ClientPackage
                protocolArtifact = $(if (-not $ClientPackage) { $protocol.artifact } else { $null })
                fixtureProtocolArtifact = $protocol.artifact
                requiredContract = @{ major = $RequiredContractMajor; minimumRevision = 0 }
            }
            server = $lock.artifact
            target = $lock.target
            scenarioContract = $lock.contract
            scenarios = $(if ($ExpectIncompatible) { @('installation-contract-rejected') } else { @($scenarios.scenarios.id) + $optionalScenarios })
            optionalScenarios = @($optionalScenarios)
            fixtureTimeoutSeconds = $fixtureTimeout
        }
        $destination = [IO.Path]::GetFullPath($EvidencePath, $repositoryRoot)
        [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($destination)) | Out-Null
        $json = ($report | ConvertTo-Json -Depth 12) + [Environment]::NewLine
        $stream = [IO.File]::Open($destination, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write)
        try { $bytes = [Text.UTF8Encoding]::new($false).GetBytes($json); $stream.Write($bytes) }
        finally { $stream.Dispose() }
    }
}
finally {
    [Environment]::SetEnvironmentVariable("BRIOSA_CONFORMANCE_EXPECT_INCOMPATIBLE", $previousExpectation)
    [Environment]::SetEnvironmentVariable("Briosa__Desktop__Mode", $previousDesktopMode)
    $resolvedTemporaryRoot = [IO.Path]::GetFullPath($temporaryRoot)
    if ($resolvedTemporaryRoot.StartsWith($temporaryBase, [StringComparison]::OrdinalIgnoreCase) -and
        (Test-Path -LiteralPath $resolvedTemporaryRoot)) {
        Remove-Item -LiteralPath $resolvedTemporaryRoot -Recurse -Force
    }
}
