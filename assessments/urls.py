"""
Assessments app URL configuration for microprojects APIs
"""

from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    # Microproject APIs
    path('api/microprojects/', views.microprojects_api, name='microprojects_list'),
    path('api/microprojects/<int:mp_id>/', views.microproject_detail_api, name='microproject_detail'),
    path('api/units/<int:unit_num>/microprojects/', views.unit_microprojects_api, name='unit_microprojects'),
    path('api/microprojects/stats/', views.microprojects_stats_api, name='microprojects_stats'),
]
