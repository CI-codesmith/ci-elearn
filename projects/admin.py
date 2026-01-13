
from django.contrib import admin
from .models import Project, ProjectMember, ProjectLead, ProjectMilestone, ProjectDeliverable

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'program', 'start_date', 'end_date')
	search_fields = ('title', 'program__code')
	list_filter = ('start_date', 'end_date')

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
	list_display = ('project', 'user_profile', 'joined_on')
	search_fields = ('project__title', 'user_profile__user__username')
	list_filter = ('project',)

@admin.register(ProjectLead)
class ProjectLeadAdmin(admin.ModelAdmin):
	list_display = ('project', 'user_profile')
	search_fields = ('project__title', 'user_profile__user__username')
	list_filter = ('project',)

@admin.register(ProjectMilestone)
class ProjectMilestoneAdmin(admin.ModelAdmin):
	list_display = ('project', 'title', 'due_date')
	search_fields = ('project__title', 'title')
	list_filter = ('project', 'due_date')

@admin.register(ProjectDeliverable)
class ProjectDeliverableAdmin(admin.ModelAdmin):
	list_display = ('milestone', 'title', 'submitted_by', 'submitted_on', 'file')
	search_fields = ('milestone__title', 'title', 'submitted_by__user__username')
	list_filter = ('milestone', 'submitted_on')
