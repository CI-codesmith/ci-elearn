
from django.db import models
from core.models import UserProfile, Role, Program, Enrollment

# SchoolStandard: 8–12
class SchoolStandard(models.Model):
	STANDARD_CHOICES = [(str(i), str(i)) for i in range(8, 13)]
	standard = models.CharField(max_length=2, choices=STANDARD_CHOICES, unique=True)

	def __str__(self):
		return f"Standard {self.standard}"

# CoachingBatch: linked to Program & year
class CoachingBatch(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='coaching_batches')
	year = models.PositiveIntegerField()
	name = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name} ({self.year}) - {self.program.code}"

# CoachingSubject
class CoachingSubject(models.Model):
	name = models.CharField(max_length=100)
	standard = models.ForeignKey(SchoolStandard, on_delete=models.CASCADE, related_name='subjects')

	def __str__(self):
		return f"{self.name} (Std {self.standard})"

# TeacherAssignment
class TeacherAssignment(models.Model):
	teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='teaching_assignments')
	subject = models.ForeignKey(CoachingSubject, on_delete=models.CASCADE, related_name='teacher_assignments')
	batch = models.ForeignKey(CoachingBatch, on_delete=models.CASCADE, related_name='teacher_assignments')

	def __str__(self):
		return f"{self.teacher} - {self.subject} - {self.batch}"

# CoachingEnrollment
class CoachingEnrollment(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='coaching_enrollments')
	batch = models.ForeignKey(CoachingBatch, on_delete=models.CASCADE, related_name='enrollments')
	year = models.PositiveIntegerField()
	status = models.CharField(max_length=20, default='active')

	def __str__(self):
		return f"{self.user_profile} - {self.batch} ({self.year})"

# CoachingFeePlan
class CoachingFeePlan(models.Model):
	batch = models.ForeignKey(CoachingBatch, on_delete=models.CASCADE, related_name='fee_plans')
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	due_date = models.DateField()

	def __str__(self):
		return f"{self.batch} - ₹{self.amount} due {self.due_date}"

# Create your models here.
