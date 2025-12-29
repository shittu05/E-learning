#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# Activate your virtual environment (optional if Render auto-activates)
# source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "initializing database migrations..."
python manage.py makemigrations --noinput

echo "Applying all migrations..."
python manage.py migrate --noinput

echo "All tasks completed successfully!"
