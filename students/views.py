from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from assessments.models import Activity, Submission
from students.models import Student
from django.contrib.auth import authenticate, login
from django.contrib import messages


@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return HttpResponse(
            "<h2>This account is not a student account.</h2>"
            "<p>Please login using a student roll-number ID.</p>"
        )

    activities = Activity.objects.all().order_by('unit', 'activity_type')
    submissions = Submission.objects.filter(student=request.user)
    
    # Build submission map: activity_id -> submission
    submission_map = {submission.activity.id: submission for submission in submissions}
    
    # Build activities data with submissions pre-attached for template
    activities_data = []
    for activity in activities:
        activities_data.append({
            'activity': activity,
            'submission': submission_map.get(activity.id),
        })

    context = {
        "student": student,
        "activities_data": activities_data,
    }

    return render(request, "students_dashboard.html", context)


def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/student/dashboard/")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "student_login.html")