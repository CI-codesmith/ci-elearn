from django.core.management.base import BaseCommand
from assessments.models import Activity, Submission


class Command(BaseCommand):
    help = 'Update submission records for specific activities with marks and completion status'

    def handle(self, *args, **options):
        # Define activities and their marks
        activity_marks_map = {
            'Practical 01 - Installation of IDE': 25,
            'Quiz 1': 4,
            'Unit 1 Assignment': 18,
        }
        
        for activity_title, marks in activity_marks_map.items():
            try:
                activity = Activity.objects.get(title=activity_title)
            except Activity.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(
                        f'Activity not found: {activity_title}'
                    )
                )
                continue
            
            # Fetch all submissions for this activity
            submissions = Submission.objects.filter(activity=activity)
            
            # Update marks and completed status
            for submission in submissions:
                submission.marks_obtained = marks
                submission.completed = True
            
            # Bulk update for efficiency
            Submission.objects.bulk_update(
                submissions,
                ['marks_obtained', 'completed'],
                batch_size=100
            )
            
            count = submissions.count()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Updated {count} submissions for {activity_title}'
                )
            )
