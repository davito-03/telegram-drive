#!/bin/sh
set -e
mkdir -p /app/downloads /home/appuser/.config/rclone
if [ "$(id -u)" = "0" ]; then
  chown -R appuser:appuser /app/downloads /home/appuser 2>/dev/null || true
  exec gosu appuser "$@"
fi
exec "$@"
