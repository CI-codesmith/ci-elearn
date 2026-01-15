from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
import os
import json


class Command(BaseCommand):
    help = "Initialize database: migrate, load data, and create superuser if needed"

    def handle(self, *args, **options):
        self.stdout.write("Starting initialization...")
        
        # Step 1: Run migrations
        self.stdout.write("Running migrations...")
        call_command('migrate', verbosity=0)
        self.stdout.write(self.style.SUCCESS('✓ Migrations complete'))
        
        # Step 2: Load data backup if it exists and DB is empty
        if not User.objects.exists():
            backup_file = 'data_backup.json'
            if os.path.exists(backup_file):
                self.stdout.write(f"Loading data from {backup_file}...")
                try:
                    call_command('loaddata', backup_file, verbosity=0)
                    self.stdout.write(self.style.SUCCESS('✓ Data loaded successfully'))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'⚠ Could not load data: {e}'))
            else:
                self.stdout.write(self.style.WARNING('⚠ No data_backup.json found'))
        else:
            self.stdout.write('✓ Database already has data, skipping load')
        
        # Step 3: Ensure superuser exists
        if not User.objects.filter(username='admin').exists():
            self.stdout.write("Creating superuser 'admin'...")
            User.objects.create_superuser(
                username='admin',
                email='admin@chatakeinnoworks.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✓ Superuser created (admin/admin123)'))
        else:
            self.stdout.write('✓ Superuser already exists')
        
        self.stdout.write(self.style.SUCCESS('\n✅ Initialization complete!'))
