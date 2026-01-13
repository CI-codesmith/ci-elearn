from .models import Program, Role

def create_initial_programs():
    programs = [
        {"code": "CI-ELEARN", "name": "CI-Elearn", "type": "project"},
        {"code": "CI-EDUSPHERE", "name": "CI-EduSphere", "type": "school"},
        {"code": "CI-INTERNSHIP", "name": "CI-Internship", "type": "internship"},
        {"code": "CI-PROJECTS", "name": "CI-Projects", "type": "project"},
    ]
    for p in programs:
        Program.objects.get_or_create(code=p["code"], defaults={"name": p["name"], "type": p["type"]})

def create_default_roles():
    Role.objects.get_or_create(name="Student", defaults={"description": "Default student role"})
