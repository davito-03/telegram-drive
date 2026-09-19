#!/bin/sh
set -e
mkdir -p /app/downloads
if [ "$(id -u)" = "0" ]; then
  chown -R appuser:appuser /app/downloads 2>/dev/null || true
  exec gosu appuser "$@"
fi
exec "$@"
