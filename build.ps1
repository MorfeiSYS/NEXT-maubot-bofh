$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$mbc = Get-Command mbc -ErrorAction SilentlyContinue
if (-not $mbc) {
    Write-Host "mbc not found. Install dev dependencies:" -ForegroundColor Yellow
    Write-Host "  pip install -r requirements-dev.txt"
    exit 1
}

if (-not $env:HOME -and $env:USERPROFILE) {
    $env:HOME = $env:USERPROFILE
}

$buildDir = Join-Path $PSScriptRoot "build"
New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

Get-ChildItem -Path $PSScriptRoot -Filter "*.mbp" -File | ForEach-Object {
    Move-Item -Path $_.FullName -Destination $buildDir -Force
}

Write-Host "Building maubot plugin into build/..."
& mbc build -o $buildDir
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Get-ChildItem -Path $buildDir -Filter "*.mbp" | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | ForEach-Object {
    Write-Host "Created: $($_.FullName)" -ForegroundColor Green
}
