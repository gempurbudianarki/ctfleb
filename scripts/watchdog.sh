#!/usr/bin/env bash
# ==============================================================================
# CCA CTF 24/7 High-Availability Health Check & Auto-Recovery Watchdog
# ==============================================================================

PROJECT_DIR="/home/ctf/htdocs/acehtanggap.cloud"
LOG_FILE="$PROJECT_DIR/logs/watchdog.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

mkdir -p "$PROJECT_DIR/logs"

# Check if Gunicorn port 8090 is responding to HTTP requests
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "http://127.0.0.1:8090/" -H "Host: acehtanggap.cloud" 2>/dev/null || echo "000")

if [ "$STATUS_CODE" = "000" ] || [ "$STATUS_CODE" = "502" ] || [ "$STATUS_CODE" = "500" ]; then
    echo "[$TIMESTAMP] [ALERT] CTFd HTTP check failed (Status: $STATUS_CODE). Initiating auto-recovery..." >> "$LOG_FILE"
    
    # Try systemd user service restart first
    systemctl --user restart ctfd.service 2>/dev/null
    sleep 3
    
    # If still down, fallback to direct background gunicorn process
    CHECK_AGAIN=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 "http://127.0.0.1:8090/" -H "Host: acehtanggap.cloud" 2>/dev/null || echo "000")
    if [ "$CHECK_AGAIN" = "000" ]; then
        echo "[$TIMESTAMP] [RECOVERY] Systemd restart failed, launching direct background daemon..." >> "$LOG_FILE"
        pkill -f "gunicorn.*8090" 2>/dev/null || true
        sleep 1
        nohup "$PROJECT_DIR/.venv/bin/gunicorn" -k gevent -w 4 --worker-connections 1000 -b 127.0.0.1:8090 wsgi:app >> "$PROJECT_DIR/logs/gunicorn.log" 2>&1 &
    fi
fi
