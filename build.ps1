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

Write-Host "Building maubot plugin..."
& mbc build
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Get-ChildItem -Filter *.mbp | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | ForEach-Object {
    Write-Host "Created: $($_.FullName)" -ForegroundColor Green
}
