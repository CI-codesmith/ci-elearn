from django.contrib import admin
from .models import UserProfile, Role, Program, Batch, Enrollment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
	search_fields = ('user__username',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ('name',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
	list_display = ('code', 'name', 'type')
	search_fields = ('code', 'name')
	list_filter = ('type',)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
	list_display = ('name', 'year', 'program')
	search_fields = ('name',)
	list_filter = ('year', 'program')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
	list_display = ('user_profile', 'program', 'batch', 'year', 'status')
	search_fields = ('user_profile__user__username', 'program__code', 'batch__name')
	list_filter = ('program', 'batch', 'year', 'status')
