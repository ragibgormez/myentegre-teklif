#!/bin/sh
set -e

echo "==> Postgres bekleniyor (host: ${POSTGRES_HOST:-db}:${POSTGRES_PORT:-5432})..."
until nc -z "${POSTGRES_HOST:-db}" "${POSTGRES_PORT:-5432}"; do
    sleep 1
done
echo "==> Postgres hazir."

echo "==> Migrations calistiriliyor..."
python manage.py migrate --noinput

echo "==> Static dosyalar toplaniyor..."
python manage.py collectstatic --noinput

echo "==> Sunucu basliyor: $@"
exec "$@"
