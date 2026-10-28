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
$hashProvider = [System.Security.Cryptography.SHA256]::Create()
try {
    $rootHash = [BitConverter]::ToString($hashProvider.ComputeHash(
        [Text.Encoding]::UTF8.GetBytes($projectRoot.ToLowerInvariant()))).Replace('-', '').Substring(0, 24)
} finally { $hashProvider.Dispose() }
$runnerMutex = [System.Threading.Mutex]::new($false, ('Local\NalarExerciseNightly_' + $rootHash))
$mutexAcquired = $false
$runnerExitCode = 0
try {
    try { $mutexAcquired = $runnerMutex.WaitOne(0) }
    catch [System.Threading.AbandonedMutexException] { $mutexAcquired = $true }
    if (-not $mutexAcquired) {
        'Another runner is active; its metadata and validation process are preserved.' | Out-File -LiteralPath $logPath -Encoding utf8
        return
    }
    $runnerMetadata = [ordered]@{
        ProcessId = $PID
        WaitForProcessId = $AfterProcessId
        RequestedRuns = 1
        StartedAt = [DateTimeOffset]::Now.ToString('o')
        LogPath = $logPath
        Status = 'starting'
    }
    $runnerMetadataPath = Join-Path $projectRoot 'runs\nightly_pipeline\active_runner.json'
    $runnerMetadata | ConvertTo-Json | Set-Content -LiteralPath $runnerMetadataPath -Encoding utf8
    if ($AfterProcessId -gt 0) {
        ('Waiting for validation process ' + $AfterProcessId + ' before nightly finalization.') | Out-File -LiteralPath $logPath -Encoding utf8
        Wait-Process -Id $AfterProcessId -ErrorAction SilentlyContinue
    }
    $runnerMetadata.Status = 'running'
    $runnerMetadata | ConvertTo-Json | Set-Content -LiteralPath $runnerMetadataPath -Encoding utf8
    & $pythonPath -X utf8 (Join-Path $PSScriptRoot 'nightly_pipeline.py') run --execute *>> $logPath
    $runnerExitCode = $LASTEXITCODE
    $runnerMetadata.Status = if ($runnerExitCode -eq 0) { 'completed' } else { 'stopped' }
    $runnerMetadata.FinishedAt = [DateTimeOffset]::Now.ToString('o')
    $runnerMetadata.ExitCode = $runnerExitCode
    $runnerMetadata | ConvertTo-Json | Set-Content -LiteralPath $runnerMetadataPath -Encoding utf8
} finally {
    if ($mutexAcquired) { $runnerMutex.ReleaseMutex() }
    $runnerMutex.Dispose()
}
exit $runnerExitCode
