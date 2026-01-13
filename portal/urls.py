from django.urls import path
from . import views

app_name = "portal"   # ✅ THIS IS THE FIX

urlpatterns = [
    path("", views.role_selector, name="role_selector"),
    path("student/", views.student_dashboard, name="student_dashboard"),
    path("teacher/", views.teacher_dashboard, name="teacher_dashboard"),
    path("intern/", views.intern_dashboard, name="intern_dashboard"),
    path("project/", views.project_dashboard, name="project_dashboard"),
    path("accounts/", views.accounts_dashboard, name="accounts_dashboard"),
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
]
