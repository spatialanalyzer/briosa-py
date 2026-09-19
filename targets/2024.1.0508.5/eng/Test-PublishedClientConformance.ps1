[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$ClientPackagePath,
    [Parameter(Mandatory)][ValidatePattern('^[a-f0-9]{64}$')][string]$ClientPackageSha256,
    [Parameter(Mandatory)][ValidatePattern('^[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?$')][string]$ClientVersion,
    [Parameter(Mandatory)][string]$ArtifactPath,
    [Parameter(Mandatory)][string]$LockPath,
    [Parameter(Mandatory)][string]$EvidencePath,
    [string]$PublishedPackageUrl,
    [string]$FixtureExecutable = 'python'
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$targetRoot = Split-Path -Parent $PSScriptRoot
$package = [IO.Path]::GetFullPath($ClientPackagePath, $targetRoot)
if ((Get-FileHash -LiteralPath $package -Algorithm SHA256).Hash.ToLowerInvariant() -cne $ClientPackageSha256) {
    throw 'Client package digest differs from the retained release record.'
}
$temporaryBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$consumer = Join-Path $temporaryBase "briosa-published-consumer-$([Guid]::NewGuid().ToString('N'))"
[IO.Directory]::CreateDirectory($consumer) | Out-Null
$previousPythonPath = [Environment]::GetEnvironmentVariable('PYTHONPATH')
try {
    $expectedName = 'briosa-2024-1-0508-5'
    $wheel = Join-Path $consumer ([IO.Path]::GetFileName($package))
    Copy-Item -LiteralPath $package -Destination $wheel
    & $FixtureExecutable -m venv (Join-Path $consumer 'venv')
    if ($LASTEXITCODE -ne 0) { throw 'Published Python consumer creation failed.' }
    $python = Join-Path $consumer 'venv/Scripts/python.exe'
    $env:PYTHONPATH = ''
    & $python -m pip install --disable-pip-version-check $wheel
    if ($LASTEXITCODE -ne 0) { throw 'Published Python consumer install failed.' }
    & $python -I -c 'import importlib.metadata,sys; assert importlib.metadata.version(sys.argv[1]) == sys.argv[2]; import importlib.resources; assert importlib.resources.files("briosa").joinpath("_protected_installation.ps1").is_file()' $expectedName $ClientVersion
    if ($LASTEXITCODE -ne 0) { throw 'Wheel identity or packaged discovery adapter is invalid.' }
    $fixture = Join-Path $consumer 'client_conformance.py'
    Copy-Item -LiteralPath (Join-Path $targetRoot 'tools/client_conformance.py') -Destination $fixture
    $arguments = @{
        ArtifactPath = $ArtifactPath; LockPath = $LockPath; EvidencePath = $EvidencePath
        FixturePath = $fixture
        ClientPackage = @{
            name = $expectedName; version = $ClientVersion; sha256 = $ClientPackageSha256
            publishedUrl = $PublishedPackageUrl
        }
    }
    $arguments.PythonExecutable = $python
    & (Join-Path $PSScriptRoot 'Test-Conformance.ps1') @arguments
}
finally {
    [Environment]::SetEnvironmentVariable('PYTHONPATH', $previousPythonPath)
    $resolved = [IO.Path]::GetFullPath($consumer)
    if (-not $resolved.StartsWith($temporaryBase, [StringComparison]::OrdinalIgnoreCase) -or $resolved -eq $temporaryBase) {
        throw 'Refusing cleanup outside the temporary consumer directory.'
    }
    if (Test-Path -LiteralPath $resolved) { Remove-Item -LiteralPath $resolved -Recurse -Force }
}

