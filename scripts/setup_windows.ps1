param(
    [string]$PythonVersion = "3.12",
    [switch]$SkipTesseract
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$VirtualEnv = Join-Path $ProjectRoot ".venv"
$Python = Join-Path $VirtualEnv "Scripts\python.exe"

if (-not (Test-Path -LiteralPath $Python)) {
    py "-$PythonVersion" -m venv $VirtualEnv
}

& $Python -m pip install --upgrade pip
& $Python -m pip install -r (Join-Path $ProjectRoot "requirements.txt")

if (-not $SkipTesseract) {
    $Tesseract = "C:\Program Files\Tesseract-OCR\tesseract.exe"
    if (-not (Test-Path -LiteralPath $Tesseract)) {
        $Winget = Get-Command winget -ErrorAction SilentlyContinue
        if (-not $Winget) {
            throw "winget tidak tersedia. Pasang Tesseract 5 secara manual atau gunakan Docker."
        }
        winget install --id UB-Mannheim.TesseractOCR --exact --silent `
            --accept-package-agreements --accept-source-agreements --disable-interactivity
    }

    $SystemTessdata = Split-Path -Parent $Tesseract | Join-Path -ChildPath "tessdata"
    $UserTessdata = Join-Path $env:LOCALAPPDATA "NalarQuestionIntelligence\tessdata"
    New-Item -ItemType Directory -Force -Path $UserTessdata | Out-Null

    foreach ($Language in @("eng", "osd")) {
        $Source = Join-Path $SystemTessdata "$Language.traineddata"
        $Destination = Join-Path $UserTessdata "$Language.traineddata"
        if ((Test-Path -LiteralPath $Source) -and -not (Test-Path -LiteralPath $Destination)) {
            Copy-Item -LiteralPath $Source -Destination $Destination
        }
    }

    $IndonesianData = Join-Path $UserTessdata "ind.traineddata"
    if (-not (Test-Path -LiteralPath $IndonesianData)) {
        Invoke-WebRequest `
            -Uri "https://github.com/tesseract-ocr/tessdata_fast/raw/refs/heads/main/ind.traineddata" `
            -OutFile $IndonesianData
    }
}

& $Python -c "import pymupdf; print('PyMuPDF', pymupdf.__version__)"
& $Python -m pytest -q
Write-Output "Setup selesai. Jalankan API atau python -m app.extraction --help dari $ProjectRoot"
