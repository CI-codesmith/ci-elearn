from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.IntegerField(default=2)
    branch = models.CharField(max_length=10, default='IT')
    roll_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
