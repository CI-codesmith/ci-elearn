
from django.db import models
from core.models import UserProfile, Role, Program

# InternProfile: extra info for internship participants
class InternProfile(models.Model):
	user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='intern_profile')
	diploma_student = models.BooleanField(default=False)
	degree_student = models.BooleanField(default=False)
	# Add more fields as needed

	def __str__(self):
		return f"InternProfile: {self.user_profile}"

# InternApplication: application to an internship program
class InternApplication(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='intern_applications')
	program = models.ForeignKey(Program, on_delete=models.CASCADE, limit_choices_to={'type': 'internship'}, related_name='intern_applications')
	applied_on = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=20, default='pending')

	def __str__(self):
		return f"{self.user_profile} - {self.program} ({self.status})"

# InternTask: tasks assigned to interns
class InternTask(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE, limit_choices_to={'type': 'internship'}, related_name='intern_tasks')
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	assigned_on = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.title} - {self.program}"

# InternSubmission: submissions for tasks
class InternSubmission(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='intern_submissions')
	task = models.ForeignKey(InternTask, on_delete=models.CASCADE, related_name='submissions')
	submitted_on = models.DateTimeField(auto_now_add=True)
	content = models.TextField(blank=True)

	def __str__(self):
		return f"{self.user_profile} - {self.task}"

# MentorAssignment: assign mentors to interns
class MentorAssignment(models.Model):
	mentor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='mentored_interns')
	intern = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='assigned_mentors')
	program = models.ForeignKey(Program, on_delete=models.CASCADE, limit_choices_to={'type': 'internship'}, related_name='mentor_assignments')

	def __str__(self):
		return f"Mentor: {self.mentor} → Intern: {self.intern} ({self.program})"

# InternCertificate: certificate issued to intern
class InternCertificate(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='intern_certificates')
	program = models.ForeignKey(Program, on_delete=models.CASCADE, limit_choices_to={'type': 'internship'}, related_name='intern_certificates')
	issued_on = models.DateField(auto_now_add=True)
	certificate_file = models.FileField(upload_to='intern_certificates/', blank=True)

	def __str__(self):
		return f"Certificate: {self.user_profile} - {self.program}"

# Create your models here.
