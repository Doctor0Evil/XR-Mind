# bootstrap.ps1 - Windows bootstrap for the Mindsoft layout
Write-Host "Creating Mindsoft Neuro-Safety IDE skeleton..."
New-Item -ItemType Directory -Force -Path ide-core\frontend\src | Out-Null
New-Item -ItemType Directory -Force -Path ide-core\backend\cmd\ide-server | Out-Null
New-Item -ItemType Directory -Force -Path neurosafety-engine\core | Out-Null
New-Item -ItemType Directory -Force -Path kernel-guard-agent\agent | Out-Null
New-Item -ItemType Directory -Force -Path xr-bci-plugins\unity\Editor | Out-Null
New-Item -ItemType Directory -Force -Path mindpattern-registry | Out-Null
Write-Host "Done."