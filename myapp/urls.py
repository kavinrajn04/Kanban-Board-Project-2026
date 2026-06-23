# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("sidebar/", views.sidebar_view, name="sidebar"),
    path("dashboard/", views.dashboard_view, name="dashboad"),
]
