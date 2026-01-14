web: gunicorn lms.wsgi:application
release: python manage.py migrate && python manage.py collectstatic --no-input
