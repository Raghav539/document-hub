#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "Database started"

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Create superuser (optional, for admin access)
echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser 'admin' created")
else:
    print("Superuser already exists")
END

# Start server
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
