
from django.contrib import admin
from .models import SchoolStandard, CoachingBatch, CoachingSubject, TeacherAssignment, CoachingEnrollment, CoachingFeePlan

@admin.register(SchoolStandard)
class SchoolStandardAdmin(admin.ModelAdmin):
	list_display = ('standard',)
	search_fields = ('standard',)

@admin.register(CoachingBatch)
class CoachingBatchAdmin(admin.ModelAdmin):
	list_display = ('name', 'year', 'program')
	search_fields = ('name',)
	list_filter = ('year', 'program')

@admin.register(CoachingSubject)
class CoachingSubjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'standard')
	search_fields = ('name',)
	list_filter = ('standard',)

@admin.register(TeacherAssignment)
class TeacherAssignmentAdmin(admin.ModelAdmin):
	list_display = ('teacher', 'subject', 'batch')
	search_fields = ('teacher__user__username', 'subject__name', 'batch__name')
	list_filter = ('batch', 'subject')

@admin.register(CoachingEnrollment)
class CoachingEnrollmentAdmin(admin.ModelAdmin):
	list_display = ('user_profile', 'batch', 'year', 'status')
	search_fields = ('user_profile__user__username', 'batch__name')
	list_filter = ('batch', 'year', 'status')

@admin.register(CoachingFeePlan)
class CoachingFeePlanAdmin(admin.ModelAdmin):
	list_display = ('batch', 'amount', 'due_date')
	list_filter = ('batch', 'due_date')
