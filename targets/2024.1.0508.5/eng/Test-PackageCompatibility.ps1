[CmdletBinding()]
param(
    [string]$PackageDirectory = 'dist',
    [string]$LegacyArtifact,
    [string]$CurrentArtifact,
    [string]$CurrentLock = 'artifacts/current-conformance/conformance.lock.json',
    [string]$PublishedArtifact,
    [string]$PublishedLock = 'published-server-conformance.lock.json',
    [string]$FixtureExecutable = 'python'
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$version = ([regex]::Match((Get-Content (Join-Path $root 'pyproject.toml') -Raw), '(?m)^version = "([^"]+)"')).Groups[1].Value
$packages = @(Get-ChildItem -LiteralPath ([IO.Path]::GetFullPath($PackageDirectory, $root)) -Filter '*.whl' -File)
if ($packages.Count -ne 1) { throw 'Expected exactly one target client package.' }
$legacy = Get-Content (Join-Path $root 'conformance.lock.json') -Raw | ConvertFrom-Json
$current = Get-Content ([IO.Path]::GetFullPath($CurrentLock, $root)) -Raw | ConvertFrom-Json
$published = Get-Content ([IO.Path]::GetFullPath($PublishedLock, $root)) -Raw | ConvertFrom-Json
if (-not $LegacyArtifact) { $LegacyArtifact = Join-Path $root "artifacts/conformance/$($legacy.artifact.file_name)" }
if (-not $CurrentArtifact) { $CurrentArtifact = Join-Path $root "artifacts/current-conformance/$($current.artifact.file_name)" }
if (-not $PublishedArtifact) { $PublishedArtifact = Join-Path $root "artifacts/published-conformance/$($published.artifact.file_name)" }
# Each server generation saves its failure diagnostics in its own folder.
$diagnosticsRoot = [Environment]::GetEnvironmentVariable('BRIOSA_CONFORMANCE_DIAGNOSTICS_DIRECTORY')
try {
    foreach ($pair in @(
        # The retained Server 0.9.2 baseline must reject this client before launch.
        @{ name = 'legacy'; artifact = $LegacyArtifact; lock = 'conformance.lock.json' },
        # The server built from the pinned generation source (Server 0.10.1 features).
        @{ name = 'current'; artifact = $CurrentArtifact; lock = $CurrentLock },
        # The published Server 0.10.0, which describes none of the 0.10.1 features.
        @{ name = 'published'; artifact = $PublishedArtifact; lock = $PublishedLock }
    )) {
        if (-not [string]::IsNullOrWhiteSpace($diagnosticsRoot)) {
            $env:BRIOSA_CONFORMANCE_DIAGNOSTICS_DIRECTORY = Join-Path $diagnosticsRoot $pair.name
        }
        $arguments = @{
            ExpectIncompatible = $pair.name -eq 'legacy'
            ClientPackagePath = $packages[0].FullName
            ClientPackageSha256 = (Get-FileHash $packages[0].FullName -Algorithm SHA256).Hash.ToLowerInvariant()
            ClientVersion = $version; ArtifactPath = $pair.artifact; LockPath = $pair.lock
            EvidencePath = Join-Path $root "artifacts/$($pair.name)-package-evidence.json"
            FixtureExecutable = $FixtureExecutable
        }
        & (Join-Path $PSScriptRoot 'Test-PublishedClientConformance.ps1') @arguments
    }
}
finally {
    if (-not [string]::IsNullOrWhiteSpace($diagnosticsRoot)) {
        $env:BRIOSA_CONFORMANCE_DIAGNOSTICS_DIRECTORY = $diagnosticsRoot
    }
}
