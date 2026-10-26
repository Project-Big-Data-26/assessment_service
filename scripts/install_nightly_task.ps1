[CmdletBinding()]
param([string]$TaskName = 'Nalar-Exercise-Nightly-0100', [switch]$CheckOnly)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$pythonPath = Join-Path $projectRoot '.venv\Scripts\python.exe'
$runnerPath = Join-Path $PSScriptRoot 'run_nightly_pipeline.ps1'
if (-not (Test-Path -LiteralPath $pythonPath -PathType Leaf)) { throw 'Project virtualenv is missing.' }
if ((Get-TimeZone).Id -ne 'SE Asia Standard Time') {
    throw 'Set the scheduler host timezone to Asia/Jakarta (SE Asia Standard Time) before installing.'
}
# Read the same schedule contract as the Python runner.
$config = Get-Content -LiteralPath (Join-Path $projectRoot 'configs\nightly_pipeline.json') -Raw | ConvertFrom-Json
if ($config.timezone -ne 'Asia/Jakarta' -or $config.schedule -ne '01:00') { throw 'Unsupported schedule config.' }
if ($CheckOnly) {
    [PSCustomObject]@{ TaskName = $TaskName; Time = '01:00 WIB daily'; Runner = $runnerPath; Logon = 'Interactive current user' } | ConvertTo-Json | Write-Output
    exit 0
}
$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing -and (@($existing.Actions | Where-Object { $_.WorkingDirectory -eq $projectRoot }).Count -eq 0)) {
    throw 'A task with this name belongs to another project; choose a different TaskName.'
}
$powershellPath = Join-Path $PSHOME 'powershell.exe'
$taskArguments = '-NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File "' + $runnerPath + '"'
$action = New-ScheduledTaskAction -Execute $powershellPath -Argument $taskArguments -WorkingDirectory $projectRoot
$trigger = New-ScheduledTaskTrigger -Daily -At '01:00'
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -WakeToRun `
    -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 23)
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal -UserId $currentUser -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings `
    -Principal $principal -Description '01:00 WIB: resume Gemini N=1 exercise validation, balanced operational export, and real-response CTT/IRT.' -Force | Out-Null
$task = Get-ScheduledTask -TaskName $TaskName
$info = Get-ScheduledTaskInfo -TaskName $TaskName
[PSCustomObject]@{ TaskName = $task.TaskName; State = $task.State; NextRunTime = $info.NextRunTime;
    Timezone = (Get-TimeZone).Id; LogonType = $task.Principal.LogonType; Runner = $runnerPath }
