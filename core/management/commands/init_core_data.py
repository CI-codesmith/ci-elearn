from django.core.management.base import BaseCommand
from core.initial_data import create_initial_programs, create_default_roles

class Command(BaseCommand):
    help = 'Initialize core app with default roles and programs.'

    def handle(self, *args, **options):
        create_default_roles()
        create_initial_programs()
        self.stdout.write(self.style.SUCCESS('Default roles and programs created.'))
