from django.contrib import admin
from django.urls import path, include
from portal.models import Company, Job
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def jobs(request):
    jobs = Job.objects.all()
    return render(request, "jobs.html", {"jobs": jobs})


def admin2(request):
    companys = Company.objects.all()
    return render(request, "admin2.html", {"companys": companys})

@login_required(login_url="login")
def jobs(request):
    jobs = Job.objects.all()
    return render(request, "jobs.html", {"jobs": jobs})


urlpatterns = [
    path('admin/', admin.site.urls),
    path("admin2/", admin2),
    path("jobs/", jobs, name="jobs"),
    path("", include("portal.urls")),
]