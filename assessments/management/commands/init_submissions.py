from django.core.management.base import BaseCommand
from students.models import Student
from assessments.models import Activity, Submission


class Command(BaseCommand):
    help = 'Initialize submission records for all students and activities'

    def handle(self, *args, **options):
        students = Student.objects.all()
        activities = Activity.objects.all()
        
        created_count = 0
        
        for student in students:
            for activity in activities:
                submission, created = Submission.objects.get_or_create(
                    student=student.user,
                    activity=activity,
                    defaults={'marks_obtained': 0}
                )
                if created:
                    created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} submission records'
            )
        )
