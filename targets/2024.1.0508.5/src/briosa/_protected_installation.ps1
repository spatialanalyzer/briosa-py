param([switch]$CheckAcl)
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
[Console]::InputEncoding = [Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [Text.UTF8Encoding]::new($false)
function Test-BriosaAcl($acl, [bool]$includeWrite) {
  $descriptor = [Security.AccessControl.RawSecurityDescriptor]::new($acl.GetSecurityDescriptorBinaryForm(), 0)
  if ($null -eq $descriptor.DiscretionaryAcl) { return $false }
  $trusted = @('S-1-5-32-544','S-1-5-18','S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464')
  if ($trusted -notcontains $acl.GetOwner([Security.Principal.SecurityIdentifier]).Value) { return $false }
  $changes = [Security.AccessControl.FileSystemRights]'Delete,DeleteSubdirectoriesAndFiles,ChangePermissions,TakeOwnership'
  if ($includeWrite) { $changes = $changes -bor [Security.AccessControl.FileSystemRights]::Write }
  foreach ($rule in $acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier])) {
    if ($rule.AccessControlType -ne 'Allow' -or ($rule.PropagationFlags -band [Security.AccessControl.PropagationFlags]::InheritOnly) -ne 0) { continue }
    $genericWrite = ([int64]$rule.FileSystemRights -band 0x50000000) -ne 0
    if ((($rule.FileSystemRights -band $changes) -ne 0 -or $genericWrite) -and $trusted -notcontains $rule.IdentityReference.Value) { return $false }
  }
  return $true
}

if ($CheckAcl) {
  $request = [Console]::In.ReadToEnd() | ConvertFrom-Json
  $acl = [Security.AccessControl.DirectorySecurity]::new()
  $acl.SetSecurityDescriptorSddlForm($request.sddl)
  [Console]::Write((Test-BriosaAcl $acl $request.includeWrite).ToString().ToLowerInvariant())
  exit
}
try {
  $path = [Console]::In.ReadToEnd() | ConvertFrom-Json
  $payload = [IO.Path]::GetDirectoryName($path)
  $pending = [Collections.Generic.Stack[IO.DirectoryInfo]]::new()
  $pending.Push([IO.DirectoryInfo]::new($payload))
  $count = 0
  while ($pending.Count -gt 0) {
    $current = $pending.Pop()
    foreach ($item in $current.EnumerateFileSystemInfos()) {
      $count++
      if ($count -gt 10000 -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw 'layout' }
      if (-not (Test-BriosaAcl (Get-Acl -LiteralPath $item.FullName) $true)) { throw 'access' }
      if ($item -is [IO.DirectoryInfo]) { $pending.Push($item) }
    }
  }
  $directory = [IO.DirectoryInfo]::new($payload)
  while ($null -ne $directory.Parent) {
    if (-not (Test-BriosaAcl (Get-Acl -LiteralPath $directory.FullName) ($directory.FullName -eq $payload))) { throw 'access' }
    $directory = $directory.Parent
  }
  [Console]::Write('true')
} catch { [Console]::Write('false') }
