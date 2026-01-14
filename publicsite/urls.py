from django.urls import path
from . import views

app_name = 'publicsite'

urlpatterns = [
    path('', views.PublicHomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('divisions/', views.DivisionsView.as_view(), name='divisions'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('internship/', views.InternshipView.as_view(), name='internship'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
