
from django.db import models
from core.models import UserProfile, Program

# Project: a project instance, linked to a Program (type=project)
class Project(models.Model):
	program = models.OneToOneField(Program, on_delete=models.CASCADE, limit_choices_to={'type': 'project'}, related_name='project')
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)

	def __str__(self):
		return f"{self.title} ({self.program.code})"

# ProjectMember: users in a project
class ProjectMember(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='project_memberships')
	joined_on = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.user_profile} in {self.project}"

# ProjectLead: lead user for a project
class ProjectLead(models.Model):
	project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='lead')
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leading_projects')

	def __str__(self):
		return f"Lead: {self.user_profile} for {self.project}"

# ProjectMilestone: milestones for a project
class ProjectMilestone(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones')
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	due_date = models.DateField()

	def __str__(self):
		return f"{self.title} ({self.project})"

# ProjectDeliverable: deliverables for a milestone
class ProjectDeliverable(models.Model):
	milestone = models.ForeignKey(ProjectMilestone, on_delete=models.CASCADE, related_name='deliverables')
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	submitted_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='project_deliverables')
	submitted_on = models.DateTimeField(null=True, blank=True)
	file = models.FileField(upload_to='project_deliverables/', blank=True)

	def __str__(self):
		return f"{self.title} ({self.milestone})"

# Create your models here.
