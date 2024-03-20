#!/bin/sh


cd portfolio/

# Run Django migrations
echo "Applying Django migrations..."
python manage.py makemigrations
python manage.py migrate --no-input
echo "Django migrations applied successfully."

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input
echo "Static files collected successfully."

# Start Gunicorn server
echo "Starting Gunicorn server..."

gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000
#python portfolio/manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT}
