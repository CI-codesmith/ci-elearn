from django.db import models
from django.contrib.auth.models import User
from courses.models import Subject


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('assignment', 'Assignment'),
        ('practical', 'Practical'),
        ('microproject', 'Microproject'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    unit = models.IntegerField()
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    max_marks = models.IntegerField()

    def __str__(self):
        return self.title


class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    marks_obtained = models.FloatField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.activity.title}"
