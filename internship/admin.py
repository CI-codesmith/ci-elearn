
from django.contrib import admin
from .models import InternProfile, InternApplication, InternTask, InternSubmission, MentorAssignment, InternCertificate

@admin.register(InternProfile)
class InternProfileAdmin(admin.ModelAdmin):
	list_display = ('user_profile', 'diploma_student', 'degree_student')
	search_fields = ('user_profile__user__username',)
	list_filter = ('diploma_student', 'degree_student')

@admin.register(InternApplication)
class InternApplicationAdmin(admin.ModelAdmin):
	list_display = ('user_profile', 'program', 'applied_on', 'status')
	search_fields = ('user_profile__user__username', 'program__code')
	list_filter = ('program', 'status')

@admin.register(InternTask)
class InternTaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'program', 'assigned_on')
	search_fields = ('title', 'program__code')
	list_filter = ('program',)

@admin.register(InternSubmission)
class InternSubmissionAdmin(admin.ModelAdmin):
	list_display = ('user_profile', 'task', 'submitted_on')
	search_fields = ('user_profile__user__username', 'task__title')
	list_filter = ('task',)

@admin.register(MentorAssignment)
class MentorAssignmentAdmin(admin.ModelAdmin):
	list_display = ('mentor', 'intern', 'program')
	search_fields = ('mentor__user__username', 'intern__user__username', 'program__code')
	list_filter = ('program',)

@admin.register(InternCertificate)
class InternCertificateAdmin(admin.ModelAdmin):
	list_display = ('user_profile', 'program', 'issued_on', 'certificate_file')
	search_fields = ('user_profile__user__username', 'program__code')
	list_filter = ('program', 'issued_on')
