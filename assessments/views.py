from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.serializers import serialize
from .models import Activity, Submission
from courses.models import Subject
import json


@require_http_methods(["GET"])
def microprojects_api(request):
    """
    API endpoint to retrieve all microprojects with unit information
    Used by website for displaying MP catalog
    """
    microprojects = Activity.objects.filter(
        activity_type='microproject'
    ).values(
        'id', 'title', 'unit', 'max_marks', 'subject__code', 'subject__name'
    ).order_by('unit', 'title')
    
    # Group by unit
    units = {}
    for mp in microprojects:
        unit = mp['unit']
        if unit not in units:
            units[unit] = {
                'unit_number': unit,
                'projects': []
            }
        units[unit]['projects'].append({
            'id': mp['id'],
            'title': mp['title'],
            'unit': mp['unit'],
            'max_marks': mp['max_marks'],
            'course_code': mp['subject__code'],
            'course_name': mp['subject__name'],
            'folder_name': f"MICROPROJECT_{mp['unit']}_{len(units[unit]['projects']) + 1}"
        })
    
    return JsonResponse({
        'success': True,
        'total_count': len(microprojects),
        'units': units,
        'microprojects': list(microprojects)
    })


@require_http_methods(["GET"])
def microproject_detail_api(request, mp_id):
    """
    API endpoint to retrieve details of a specific microproject
    """
    try:
        microproject = Activity.objects.get(
            id=mp_id,
            activity_type='microproject'
        )
        
        return JsonResponse({
            'success': True,
            'microproject': {
                'id': microproject.id,
                'title': microproject.title,
                'unit': microproject.unit,
                'max_marks': microproject.max_marks,
                'course': {
                    'code': microproject.subject.code,
                    'name': microproject.subject.name
                }
            }
        })
    except Activity.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Microproject not found'
        }, status=404)


@require_http_methods(["GET"])
def unit_microprojects_api(request, unit_num):
    """
    API endpoint to retrieve all microprojects for a specific unit
    """
    microprojects = Activity.objects.filter(
        unit=unit_num,
        activity_type='microproject'
    ).values(
        'id', 'title', 'unit', 'max_marks', 'subject__code', 'subject__name'
    ).order_by('title')
    
    return JsonResponse({
        'success': True,
        'unit': unit_num,
        'count': len(microprojects),
        'microprojects': list(microprojects)
    })


@require_http_methods(["GET"])
def microprojects_stats_api(request):
    """
    API endpoint to retrieve statistics about microprojects
    """
    microprojects = Activity.objects.filter(activity_type='microproject')
    
    stats = {
        'total_microprojects': microprojects.count(),
        'total_units': microprojects.values('unit').distinct().count(),
        'by_unit': {}
    }
    
    for unit in microprojects.values('unit').distinct():
        unit_num = unit['unit']
        unit_mps = microprojects.filter(unit=unit_num)
        stats['by_unit'][unit_num] = unit_mps.count()
    
    return JsonResponse({
        'success': True,
        'statistics': stats
    })
