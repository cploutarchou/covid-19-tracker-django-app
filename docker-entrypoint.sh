#!/bin/bash
python manage.py runserver 0.0.0.0:8080
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Run make migrations
echo "Collect static files"
python manage.py makemigrations --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate