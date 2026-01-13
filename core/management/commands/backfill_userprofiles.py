from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import UserProfile, Role


class Command(BaseCommand):
    help = "Backfill UserProfile for all existing users and assign Student role"

    def handle(self, *args, **options):
        student_role, _ = Role.objects.get_or_create(name="Student")
        created = 0
        for user in User.objects.all():
            profile, is_new = UserProfile.objects.get_or_create(user=user)
            if is_new or student_role not in profile.roles.all():
                profile.roles.add(student_role)
                created += 1
        self.stdout.write(self.style.SUCCESS(
            f"UserProfiles ensured for {User.objects.count()} users, Student role assigned to {created} profiles."
        ))
