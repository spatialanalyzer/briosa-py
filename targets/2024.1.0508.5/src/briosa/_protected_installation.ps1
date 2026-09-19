$ErrorActionPreference = 'Stop'
[Console]::InputEncoding = [Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [Text.UTF8Encoding]::new($false)
try {
  $path = [Console]::In.ReadToEnd() | ConvertFrom-Json
  $payload = [IO.Path]::GetDirectoryName($path)
  $paths = @('manifest.json','Briosa.Server.exe','Briosa.Worker.exe') | ForEach-Object { [IO.Path]::Combine($payload, $_) }
  $directory = [IO.DirectoryInfo]::new($payload)
  while ($null -ne $directory.Parent) { $paths += $directory.FullName; $directory = $directory.Parent }
  $trusted = @('S-1-5-32-544','S-1-5-18')
  $write = [Security.AccessControl.FileSystemRights]'Write,Delete,DeleteSubdirectoriesAndFiles,ChangePermissions,TakeOwnership'
  foreach ($item in $paths) {
    $acl = Get-Acl -LiteralPath $item
    if ($trusted -notcontains $acl.GetOwner([Security.Principal.SecurityIdentifier]).Value) { throw 'owner' }
    foreach ($rule in $acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier])) {
      if ($rule.AccessControlType -eq 'Allow' -and ($rule.FileSystemRights -band $write) -ne 0 -and $trusted -notcontains $rule.IdentityReference.Value) { throw 'access' }
    }
  }
  [Console]::Write('true')
} catch { [Console]::Write('false') }
