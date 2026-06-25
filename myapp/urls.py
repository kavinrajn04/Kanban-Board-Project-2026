# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("notes/", views.notes_view, name="notes"),
    path("notes/save/", views.save_note, name="save_note"),
]
