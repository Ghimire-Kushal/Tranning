from django.urls import path
from . import views          # ← this one is CORRECT here, in portal/urls.py

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]