#!/bin/sh
set -e

echo "==> Postgres bekleniyor (${POSTGRES_HOST:-db}:${POSTGRES_PORT:-5432})..."
python -c "
import socket, time, os, sys
host = os.environ.get('POSTGRES_HOST', 'db')
port = int(os.environ.get('POSTGRES_PORT', '5432'))
deadline = time.time() + 60
while time.time() < deadline:
    try:
        with socket.create_connection((host, port), timeout=2):
            sys.exit(0)
    except OSError:
        time.sleep(1)
sys.exit('Postgres baglanti zaman asimi')
"
echo "==> Postgres hazir."

echo "==> Migrations calistiriliyor..."
python manage.py migrate --noinput

echo "==> Static dosyalar toplaniyor..."
python manage.py collectstatic --noinput

echo "==> Sunucu basliyor: $@"
exec "$@"
