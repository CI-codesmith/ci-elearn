
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.models import UserProfile, Role

ROLE_DASHBOARD_MAP = {
	'Student': 'portal:student_dashboard',
	'Teacher': 'portal:teacher_dashboard',
	'Intern': 'portal:intern_dashboard',
	'Project': 'portal:project_dashboard',
	'Accounts': 'portal:accounts_dashboard',
	'Admin': 'portal:admin_dashboard',
}

@login_required
def role_selector(request):
	profile, _ = UserProfile.objects.get_or_create(user=request.user)
	roles = profile.roles.all()
	role_list = []
	for role in roles:
		url_name = ROLE_DASHBOARD_MAP.get(role.name, 'portal:student_dashboard')
		role_list.append({
			'name': role.name,
			'description': role.description,
			'redirect_url': reverse(url_name)
		})
	if len(role_list) == 1:
		return redirect(role_list[0]['redirect_url'])
	if request.method == 'POST':
		selected_role = request.POST.get('role')
		if selected_role in ROLE_DASHBOARD_MAP:
			request.session['active_role'] = selected_role
			return redirect(reverse(ROLE_DASHBOARD_MAP[selected_role]))
	return render(request, 'portal/role_selector.html', {'roles': role_list})

@login_required
def student_dashboard(request):
	return _dashboard(request, 'Student')

@login_required
def teacher_dashboard(request):
	return _dashboard(request, 'Teacher')

@login_required
def intern_dashboard(request):
	return _dashboard(request, 'Intern')

@login_required
def project_dashboard(request):
	return _dashboard(request, 'Project')

@login_required
def accounts_dashboard(request):
	return _dashboard(request, 'Accounts')

@login_required
def admin_dashboard(request):
	return _dashboard(request, 'Admin')

def _dashboard(request, role_name):
	profile, _ = UserProfile.objects.get_or_create(user=request.user)
	enrollments = profile.enrollments.select_related('program', 'batch').all()
	active_role = request.session.get('active_role', role_name)
	return render(request, 'portal/dashboard_base.html', {
		'role': active_role,
		'enrollments': enrollments,
	})
from django.shortcuts import render

# Create your views here.
