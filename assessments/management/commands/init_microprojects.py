"""
Django management command to initialize microprojects in the LMS database
This command creates Activity records for all 24 microprojects
"""

from django.core.management.base import BaseCommand
from courses.models import Subject
from assessments.models import Activity

MICROPROJECT_DATA = [
    # Unit 1
    {"mp_id": "1_1", "unit": 1, "title": "Data Exploration Dashboard", "max_marks": 100},
    {"mp_id": "1_2", "unit": 1, "title": "Python ML Libraries Mastery", "max_marks": 100},
    {"mp_id": "1_3", "unit": 1, "title": "Traditional vs ML Comparison", "max_marks": 100},
    {"mp_id": "1_4", "unit": 1, "title": "Dataset Curation Project", "max_marks": 100},
    # Unit 2
    {"mp_id": "2_1", "unit": 2, "title": "Data Cleaning & Preprocessing", "max_marks": 100},
    {"mp_id": "2_2", "unit": 2, "title": "Handling Missing Values", "max_marks": 100},
    {"mp_id": "2_3", "unit": 2, "title": "Data Encoding & Scaling", "max_marks": 100},
    {"mp_id": "2_4", "unit": 2, "title": "Feature Engineering Basics", "max_marks": 100},
    {"mp_id": "2_5", "unit": 2, "title": "Data Visualization & Analysis", "max_marks": 100},
    # Unit 3
    {"mp_id": "3_1", "unit": 3, "title": "Feature Selection Methods", "max_marks": 100},
    {"mp_id": "3_2", "unit": 3, "title": "Correlation Analysis", "max_marks": 100},
    {"mp_id": "3_3", "unit": 3, "title": "Removing Irrelevant Features", "max_marks": 100},
    # Unit 4
    {"mp_id": "4_1", "unit": 4, "title": "Classification Algorithms", "max_marks": 100},
    {"mp_id": "4_2", "unit": 4, "title": "Regression Algorithms", "max_marks": 100},
    {"mp_id": "4_3", "unit": 4, "title": "Model Evaluation & Metrics", "max_marks": 100},
    # Unit 5
    {"mp_id": "5_1", "unit": 5, "title": "Clustering Techniques", "max_marks": 100},
    {"mp_id": "5_2", "unit": 5, "title": "Clustering Comparison", "max_marks": 100},
    {"mp_id": "5_3", "unit": 5, "title": "PCA & Dimensionality Reduction", "max_marks": 100},
    # Unit 6
    {"mp_id": "6_1", "unit": 6, "title": "ML Ethics & Bias", "max_marks": 100},
    {"mp_id": "6_2", "unit": 6, "title": "Model Deployment & Production", "max_marks": 100},
    {"mp_id": "6_3", "unit": 6, "title": "Real-World ML Applications", "max_marks": 100},
    # Advanced
    {"mp_id": "ADV_1", "unit": 7, "title": "End-to-End ML Pipeline with Production", "max_marks": 100},
    {"mp_id": "ADV_2", "unit": 7, "title": "Deep Learning for Image Classification", "max_marks": 100},
    {"mp_id": "ADV_3", "unit": 7, "title": "Time Series Forecasting (ARIMA & LSTM)", "max_marks": 100},
]


class Command(BaseCommand):
    help = 'Initialize microprojects in the LMS database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing microprojects before creating new ones',
        )

    def handle(self, *args, **options):
        # Get or create the Machine Learning subject
        subject, created = Subject.objects.get_or_create(
            code='316316',
            defaults={'name': 'Machine Learning'}
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Created subject: {subject}')
            )
        else:
            self.stdout.write(f'Using existing subject: {subject}')

        # Clear existing microprojects if requested
        if options['clear']:
            deleted_count, _ = Activity.objects.filter(
                subject=subject,
                activity_type='microproject'
            ).delete()
            self.stdout.write(
                self.style.WARNING(f'Deleted {deleted_count} existing microprojects')
            )

        # Create microprojects
        created_count = 0
        existing_count = 0
        
        for mp_data in MICROPROJECT_DATA:
            activity, created = Activity.objects.get_or_create(
                subject=subject,
                title=mp_data['title'],
                unit=mp_data['unit'],
                activity_type='microproject',
                defaults={'max_marks': mp_data['max_marks']}
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created: {mp_data["mp_id"]} - {mp_data["title"]}'
                    )
                )
            else:
                existing_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Microprojects initialization complete!'
            )
        )
        self.stdout.write(f'  Created: {created_count} new activities')
        self.stdout.write(f'  Existing: {existing_count} activities')
        self.stdout.write(f'  Total: {created_count + existing_count} microprojects')
