#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')
django.setup()

from django.contrib.auth.models import User

# Check if admin exists
admin_user = User.objects.filter(username='admin').first()

if admin_user:
    print(f"Admin user already exists:")
    print(f"  Username: admin")
    print(f"  Email: {admin_user.email}")
else:
    # Create admin user
    User.objects.create_superuser(
        username='admin',
        email='admin@chatakeinnoworks.com',
        password='admin123'
    )
    print("✓ Admin user created!")
    print("  Username: admin")
    print("  Password: admin123")
    print("  Email: admin@chatakeinnoworks.com")
