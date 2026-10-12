#!/usr/bin/env bash
# Start any working tunnel for a local port, print public URL. Usage: bash start-tunnel.sh 5173
set -euo pipefail
PORT="${1:-5173}"
if ! curl -sf -o /dev/null "http://localhost:${PORT}"; then
  echo "Frontend NOT responding on :${PORT}. Start it first: npm run dev -- --host --port ${PORT}" >&2; exit 1
fi
if command -v cloudflared >/dev/null; then
  echo "Starting cloudflared quick tunnel..." >&2
  exec cloudflared tunnel --url "http://localhost:${PORT}"
elif command -v ngrok >/dev/null; then
  echo "cloudflared missing, using ngrok..." >&2
  exec ngrok http "${PORT}"
else
  echo "No cloudflared/ngrok. Falling back to localtunnel (desktop-only)..." >&2
  exec npx localtunnel --port "${PORT}"
fi
