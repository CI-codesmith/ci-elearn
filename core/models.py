
from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Program(models.Model):
	PROGRAM_TYPES = [
		('school', 'School'),
		('coaching', 'Coaching'),
		('internship', 'Internship'),
		('project', 'Project'),
	]
	code = models.CharField(max_length=30, unique=True)
	name = models.CharField(max_length=100)
	type = models.CharField(max_length=20, choices=PROGRAM_TYPES)

	def __str__(self):
		return f"{self.code} - {self.name}"


class Batch(models.Model):
	name = models.CharField(max_length=100)
	year = models.PositiveIntegerField()
	program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='batches')

	def __str__(self):
		return f"{self.name} ({self.year}) - {self.program.code}"


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	roles = models.ManyToManyField(Role, blank=True)
	# Add more fields as needed (phone, photo, etc.)

	def __str__(self):
		return self.user.username


class Enrollment(models.Model):
	STATUS_CHOICES = [
		('active', 'Active'),
		('inactive', 'Inactive'),
		('completed', 'Completed'),
		('dropped', 'Dropped'),
	]
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='enrollments')
	program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='enrollments')
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='enrollments')
	year = models.PositiveIntegerField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

	def __str__(self):
		return f"{self.user_profile} - {self.program.code} - {self.batch.name} ({self.year})"
