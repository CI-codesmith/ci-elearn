from django.shortcuts import render
from django.views.generic import TemplateView

class PublicHomeView(TemplateView):
    """Public home page with company overview and divisions"""
    template_name = 'publicsite/home.html'

class AboutView(TemplateView):
    """Company about page"""
    template_name = 'publicsite/about.html'

class DivisionsView(TemplateView):
    """Divisions overview"""
    template_name = 'publicsite/divisions.html'

class ProjectsView(TemplateView):
    """Projects showcase"""
    template_name = 'publicsite/projects.html'

class InternshipView(TemplateView):
    """Internship program overview"""
    template_name = 'publicsite/internship.html'

class ContactView(TemplateView):
    """Contact page"""
    template_name = 'publicsite/contact.html'
