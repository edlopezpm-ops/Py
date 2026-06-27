$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot

py -m pip install -r requirements.txt
py -m pip install -r requirements-build.txt

py -m PyInstaller `
    --noconfirm `
    --clean `
    --onedir `
    --windowed `
    --name "CVLocalGenerator" `
    "desktop_app.py"

$DistApp = Join-Path $ProjectRoot "dist\CVLocalGenerator"
foreach ($Folder in @("core", "jobs", "data", "docs")) {
    $Source = Join-Path $ProjectRoot $Folder
    if (Test-Path $Source) {
        Copy-Item -LiteralPath $Source -Destination $DistApp -Recurse -Force
    }
}

Copy-Item -LiteralPath (Join-Path $ProjectRoot "README.md") -Destination $DistApp -Force
New-Item -ItemType Directory -Force -Path (Join-Path $DistApp "output\pdf") | Out-Null

Write-Host ""
Write-Host "Build listo:"
Write-Host (Join-Path $DistApp "CVLocalGenerator.exe")
Write-Host ""
Write-Host "Distribuye toda la carpeta dist\CVLocalGenerator, no solo el .exe."
