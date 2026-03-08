#!/bin/sh

echo "Running migrations"
python manage.py migrate

echo "Creating superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
"

if [ "$DJANGO_DEBUG" = "1" ]; then
    echo "Starting server..."
    python manage.py runserver 0.0.0.0:8000
else
    echo "Collecting static files..."
    python manage.py collectstatic --noinput

    echo "Starting server..."
    gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 4
fi