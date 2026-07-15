from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application
from .forms import ApplicationForm

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created! Please log in.")
        return redirect("login")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("jobs")
        messages.error(request, "Invalid username or password")
        return redirect("login")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    already_applied = (
        request.user.is_authenticated
        and Application.objects.filter(job=job, applicant=request.user).exists()
    )
    return render(request, "job_detail.html", {"job": job, "already_applied": already_applied})

# def user_register_view(request):
#     form = UserRegisterForm()
#     return render(request, "register.html", {"form" : form})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.info(request, "You have already applied for this job.")
        return redirect("job_detail", job_id=job.id)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect("job_detail", job_id=job.id)
    else:
        form = ApplicationForm(initial={
            "full_name": request.user.get_full_name() or request.user.username,
            "email": request.user.email,
        })

    return render(request, "apply.html", {"form": form, "job": job})



# from django.shortcuts import render, redirect

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, logout

# from portal.models import Job
# from .forms import ApplicantForm, UserRegisterForm, UserLoginForm

# from django.contrib.auth import get_user_model
# User = get_user_model()
# # Create your views here.

# def job_detail(request, pk):
#     jobbbb = Job.objects.get(id=pk)
#     return render(request, "job_detail.html", 
#                   {"job": jobbbb, "form": ApplicantForm()})

# @login_required # decorators
# def handle_applicant(request, pk):
#     job = Job.objects.get(id=pk)
#     form = ApplicantForm(request.POST, request.FILES)
#     if form.is_valid():
#         applicant = form.save(commit=False)
#         applicant.job = job
#         applicant.applicant = request.user
#         applicant.save()
#     else:
#         print(form.errors)
#     return redirect("job_detail", pk=pk)


# def user_logout_view(request):
#     logout(request)
#     return redirect("/")


# def user_register_view(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = User.objects.create(
#                 username=data.get("username"),
#                 email=data.get("email")
#             )
#             user.set_password(data.get("password"))
#             user.save()
#             return redirect("login")
#     else:
#         form = UserRegisterForm()

#     return render(request, "register.html", {"form": form})


# def user_login_view(request):
#     if request.method == "POST":
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             try:
#                 user = User.objects.get(
#                     username=form.cleaned_data.get("username")
#                 )
#             except User.DoesNotExist:
#                 #TODO: message invalid username
#                 return redirect("login")
#             if user.check_password(form.cleaned_data.get("password")):
#                 login(request, user)
#                 return redirect("jobs")
#             else:
#                 # TODO: Message invalid password
#                 return redirect("login")
#     else:
#         form = UserLoginForm()

#     return render(request, "login.html", {"form": form})