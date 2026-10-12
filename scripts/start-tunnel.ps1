#Requires -Version 5.1
param([int]$Port = 5173)
# Start any working tunnel for a local port. Usage: .\start-tunnel.ps1 -Port 5173
$ErrorActionPreference = 'Stop'
try { Invoke-WebRequest -Uri "http://localhost:$Port" -UseBasicParsing -TimeoutSec 5 | Out-Null; Write-Host 'Frontend OK.' -ForegroundColor Green }
catch { Write-Host "Frontend NOT responding on :$Port. Start it first: npm run dev -- --host --port $Port" -ForegroundColor Red; exit 1 }
if (Get-Command cloudflared -ErrorAction SilentlyContinue) { & cloudflared tunnel --url "http://localhost:$Port" }
elseif (Get-Command ngrok -ErrorAction SilentlyContinue) { & ngrok http $Port }
else { npx localtunnel --port $Port }
