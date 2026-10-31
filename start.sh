#!/usr/bin/env bash
set -euo pipefail
python manage.py migrate --noinput
python manage.py seed_portfolio
python manage.py bootstrap_owner
exec gunicorn backend.wsgi:application --bind "0.0.0.0:${PORT:-8000}" --workers 2 --timeout 60
