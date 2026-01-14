from django.urls import path
from . import views

app_name = 'publiccatalog'

urlpatterns = [
    # PUBLIC ROUTES - NO LOGIN REQUIRED
    
    # Course listing
    path('courses/', views.course_list, name='course_list'),
    
    # Course detail (subject landing)
    path('courses/<str:subject_slug>/', views.course_detail, name='course_detail'),
    
    # Units list and detail
    path('courses/<str:subject_slug>/units/', views.course_detail, name='units_list'),
    path('courses/<str:subject_slug>/unit-<str:unit_slug>/', views.unit_detail, name='unit_detail'),
    
    # Podcast
    path('courses/<str:subject_slug>/podcast/', views.podcast_section, name='podcast_section'),
    path('podcast/', views.podcast_section, {'subject_slug': 'machine-learning'}, name='podcast_main'),
    
    # API endpoints (JSON)
    path('api/subjects/', views.api_subjects, name='api_subjects'),
    path('api/subjects/<str:subject_slug>/', views.api_subject_detail, name='api_subject_detail'),
]

