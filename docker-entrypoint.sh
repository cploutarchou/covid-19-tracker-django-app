#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Run makemigrations
echo "Collect static files"
python manage.py makemigrations --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate