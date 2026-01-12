from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Student


class Command(BaseCommand):
    help = "Bulk create students for Machine Learning across branches"

    def handle(self, *args, **kwargs):
        year = "2026"
        subject_code = "ML"
        password = "316316"

        branches = {
            "IF": range(3601, 3672),            # Information Technology
            "COM": list(range(3201, 3301)) + [3501],  # Computer Science A + B
        }

        for branch, roll_list in branches.items():
            for roll in roll_list:
                username = f"{year}{branch}{subject_code}{roll}"

                if User.objects.filter(username=username).exists():
                    self.stdout.write(f"User {username} already exists")
                    continue

                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                Student.objects.create(
                    user=user,
                    year=year,
                    branch=branch,
                    roll_number=str(roll)
                )

                self.stdout.write(self.style.SUCCESS(f"Created {username}"))

        self.stdout.write(self.style.SUCCESS("Student creation completed"))
