param(
    [switch]$Web,
    [switch]$Check,
    [switch]$Install
)

$ErrorActionPreference = "Stop"

$Project = Split-Path -Parent $MyInvocation.MyCommand.Path
$Requirements = Join-Path $Project "requirements.txt"
$DesktopApp = Join-Path $Project "desktop_app.py"
$WebApp = Join-Path $Project "cv_app.py"

function Install-Dependencies {
    Write-Host "Instalando dependencias de CV Local Generator..."
    py -m pip install -r $Requirements
}

function Test-Dependencies {
    py -c "import reportlab" 2>$null
    return $LASTEXITCODE -eq 0
}

Push-Location $Project
try {
    if ($Install -or -not (Test-Dependencies)) {
        Install-Dependencies
    }

    if ($Check) {
        py -m py_compile $WebApp $DesktopApp
        py -c "import cv_app; cv_app.ensure_dirs(); job=cv_app.read_job_file(cv_app.JOBS_DIR/'sample-job.txt'); package=cv_app.build_application_package(job); print('Assessment score:', package['assessment']['score']); print('PDF files:', ', '.join(item['kind'] for item in package['files']))"
        exit $LASTEXITCODE
    }

    if ($Web) {
        py $WebApp
    } else {
        py $DesktopApp
    }
}
finally {
    Pop-Location
}
