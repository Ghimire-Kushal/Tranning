"""
URL configuration for jobportal project.
"""
from django.contrib import admin
from django.urls import path, include
from portal.models import Company, Job
from django.shortcuts import render


def admin2(request):
    companys = Company.objects.all()  # select * from company
    return render(request, "admin2.html", {"companys": companys})

def jobs(request):
    jobs = Job.objects.all()   # select * from job
    return render(request, "jobs.html", {"jobs": jobs})


urlpatterns = [
    path('admin/', admin.site.urls),
    path("admin2/", admin2),
    path("jobs/", jobs, name="jobs"),
    path("", include("portal.urls")),   # login / register / logout
]