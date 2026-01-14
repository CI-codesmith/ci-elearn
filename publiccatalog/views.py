import os
import markdown
from pathlib import Path
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


# PATH TO SUBJECT CONTENT (READ-ONLY FROM FILESYSTEM)
SUBJECTS_ROOT = Path('/Users/akashchatake/Downloads/Chatake-Innoworks-Organization/ci-elearn/subjects')


class SubjectLoader:
    """Load subject content from filesystem (read-only)"""
    
    @staticmethod
    def get_all_subjects():
        """Get list of all subjects"""
        subjects = []
        if SUBJECTS_ROOT.exists():
            for subject_dir in SUBJECTS_ROOT.iterdir():
                if subject_dir.is_dir():
                    index_file = subject_dir / 'index.md'
                    if index_file.exists():
                        subjects.append({
                            'slug': subject_dir.name,
                            'name': subject_dir.name.replace('-', ' ').title(),
                            'path': subject_dir
                        })
        return sorted(subjects, key=lambda x: x['name'])
    
    @staticmethod
    def get_subject(slug):
        """Get single subject by slug"""
        subject_path = SUBJECTS_ROOT / slug
        if not subject_path.exists():
            return None
        
        index_file = subject_path / 'index.md'
        if not index_file.exists():
            return None
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {
            'slug': slug,
            'name': slug.replace('-', ' ').title(),
            'path': subject_path,
            'content': content,
            'content_html': markdown.markdown(content),
        }
    
    @staticmethod
    def get_units(slug):
        """Get all units for a subject"""
        subject_path = SUBJECTS_ROOT / slug
        units_dir = subject_path / 'units'
        
        units = []
        if units_dir.exists():
            unit_files = sorted(units_dir.glob('*.md'))
            for i, unit_file in enumerate(unit_files, 1):
                with open(unit_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract first line as title
                lines = content.split('\n')
                title = lines[0].replace('#', '').strip() if lines else 'Unit ' + str(i)
                
                units.append({
                    'number': i,
                    'slug': unit_file.stem,
                    'title': title,
                    'filename': unit_file.name,
                    'path': unit_file,
                })
        
        return units
    
    @staticmethod
    def get_unit(slug, unit_slug):
        """Get single unit content"""
        subject_path = SUBJECTS_ROOT / slug
        unit_file = subject_path / 'units' / f'{unit_slug}.md'
        
        if not unit_file.exists():
            return None
        
        with open(unit_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get unit number from slug
        unit_num = unit_slug.split('-')[1] if '-' in unit_slug else '1'
        
        return {
            'slug': unit_slug,
            'number': unit_num,
            'content': content,
            'content_html': markdown.markdown(content),
            'path': unit_file,
        }
    
    @staticmethod
    def get_notes(slug, unit_slug):
        """Get notes for a unit"""
        subject_path = SUBJECTS_ROOT / slug
        unit_num = unit_slug.split('-')[1] if '-' in unit_slug else '1'
        
        notes_dir = subject_path / 'notes' / f'unit-{unit_num}'
        notes_list = []
        
        if notes_dir.exists():
            # Check for markdown notes
            md_file = notes_dir / f'unit-{unit_num}-notes.md'
            if md_file.exists():
                with open(md_file, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                notes_list.append({
                    'type': 'markdown',
                    'filename': md_file.name,
                    'content': md_content,
                    'content_html': markdown.markdown(md_content),
                })
            
            # Check for PDF notes
            pdf_file = notes_dir / f'unit-{unit_num}-notes.pdf'
            if pdf_file.exists():
                notes_list.append({
                    'type': 'pdf',
                    'filename': pdf_file.name,
                    'url': f'/media/notes/{slug}/unit-{unit_num}/{pdf_file.name}',
                })
        
        return notes_list
    
    @staticmethod
    def get_podcasts(slug):
        """Get podcasts for a subject"""
        subject_path = SUBJECTS_ROOT / slug
        podcasts_dir = subject_path / 'podcasts'
        
        podcasts = []
        if podcasts_dir.exists():
            for podcast_file in sorted(podcasts_dir.glob('*.md')):
                with open(podcast_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                podcasts.append({
                    'filename': podcast_file.name,
                    'content': content,
                    'content_html': markdown.markdown(content),
                })
        
        return podcasts


# PUBLIC VIEWS - NO LOGIN REQUIRED

def course_list(request):
    """Public list of all courses/subjects"""
    subjects = SubjectLoader.get_all_subjects()
    context = {
        'page_title': 'Courses & Learning Subjects',
        'subjects': subjects,
        'total_subjects': len(subjects),
    }
    return render(request, 'publiccatalog/course_list_new.html', context)


def course_detail(request, subject_slug):
    """Public course landing page"""
    subject = SubjectLoader.get_subject(subject_slug)
    if not subject:
        return redirect('publiccatalog:course_list')
    
    units = SubjectLoader.get_units(subject_slug)
    podcasts = SubjectLoader.get_podcasts(subject_slug)
    
    context = {
        'page_title': subject['name'],
        'subject': subject,
        'units': units,
        'podcasts': podcasts,
        'total_units': len(units),
    }
    return render(request, 'publiccatalog/course_detail_new.html', context)


def unit_detail(request, subject_slug, unit_slug):
    """Public unit detail page with notes and podcast"""
    subject = SubjectLoader.get_subject(subject_slug)
    if not subject:
        return redirect('publiccatalog:course_list')
    
    unit = SubjectLoader.get_unit(subject_slug, unit_slug)
    if not unit:
        return redirect('publiccatalog:course_detail', subject_slug=subject_slug)
    
    notes = SubjectLoader.get_notes(subject_slug, unit_slug)
    units = SubjectLoader.get_units(subject_slug)
    podcasts = SubjectLoader.get_podcasts(subject_slug)
    
    # Find current unit index for navigation
    unit_index = None
    for i, u in enumerate(units):
        if u['slug'] == unit_slug:
            unit_index = i
            break
    
    prev_unit = units[unit_index - 1] if unit_index and unit_index > 0 else None
    next_unit = units[unit_index + 1] if unit_index is not None and unit_index < len(units) - 1 else None
    
    context = {
        'page_title': f'{subject["name"]} - {unit["slug"].replace("-", " ").title()}',
        'subject': subject,
        'unit': unit,
        'notes': notes,
        'podcasts': podcasts,
        'units': units,
        'prev_unit': prev_unit,
        'next_unit': next_unit,
        'current_unit_number': unit_index + 1 if unit_index is not None else 1,
        'total_units': len(units),
    }
    return render(request, 'publiccatalog/unit_detail_new.html', context)


def podcast_section(request, subject_slug):
    """Public podcast page for a subject"""
    subject = SubjectLoader.get_subject(subject_slug)
    if not subject:
        return redirect('publiccatalog:course_list')
    
    podcasts = SubjectLoader.get_podcasts(subject_slug)
    
    context = {
        'page_title': f'{subject["name"]} - Podcast',
        'subject': subject,
        'podcasts': podcasts,
    }
    return render(request, 'publiccatalog/podcast.html', context)


@require_http_methods(["GET"])
def api_subjects(request):
    """JSON API - List all subjects"""
    subjects = SubjectLoader.get_all_subjects()
    return JsonResponse({
        'count': len(subjects),
        'subjects': [
            {'slug': s['slug'], 'name': s['name']}
            for s in subjects
        ]
    })


@require_http_methods(["GET"])
def api_subject_detail(request, subject_slug):
    """JSON API - Subject details with units"""
    subject = SubjectLoader.get_subject(subject_slug)
    if not subject:
        return JsonResponse({'error': 'Subject not found'}, status=404)
    
    units = SubjectLoader.get_units(subject_slug)
    
    return JsonResponse({
        'slug': subject['slug'],
        'name': subject['name'],
        'units': [
            {'number': u['number'], 'slug': u['slug'], 'title': u['title']}
            for u in units
        ]
    })


