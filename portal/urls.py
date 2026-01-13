from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_selector, name='portal_role_selector'),
    path('student/', views.student_dashboard, name='portal_student_dashboard'),
    path('teacher/', views.teacher_dashboard, name='portal_teacher_dashboard'),
    path('intern/', views.intern_dashboard, name='portal_intern_dashboard'),
    path('project/', views.project_dashboard, name='portal_project_dashboard'),
    path('accounts/', views.accounts_dashboard, name='portal_accounts_dashboard'),
    path('admin/', views.admin_dashboard, name='portal_admin_dashboard'),
]
