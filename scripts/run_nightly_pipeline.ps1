[CmdletBinding()]
param([int]$AfterProcessId = 0)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $projectRoot
$pythonPath = Join-Path $projectRoot '.venv\Scripts\python.exe'
$logDirectory = Join-Path $projectRoot 'runs\nightly_pipeline\scheduler_logs'
New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null
$runStamp = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfffffffZ')
$logPath = Join-Path $logDirectory ($runStamp + '.log')
if ($AfterProcessId -gt 0) {
    ('Waiting for validation process ' + $AfterProcessId + ' before nightly finalization.') | Out-File -LiteralPath $logPath -Encoding utf8
    Wait-Process -Id $AfterProcessId -ErrorAction SilentlyContinue
}
& $pythonPath -X utf8 (Join-Path $PSScriptRoot 'nightly_pipeline.py') run --execute *>> $logPath
exit $LASTEXITCODE
