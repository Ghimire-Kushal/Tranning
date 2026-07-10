from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# models for company and job
class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    location = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to="resumes/")
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("job", "applicant")
        ordering = ["-applied_at"]

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"