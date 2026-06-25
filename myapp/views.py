from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Note

# Create your views here.
# myapp/views.py


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("notes")  # wherever you want to send them after login
        else:
            return render(request, "login-page.html", {"error": "Invalid credentials"})
    return render(request, "login-page.html")


def notes_view(request):
    return render(request, "notes-view.html", {"username": request.user.username})


@csrf_exempt
def save_note(request):
    data = json.loads(request.body)
    note = Note.objects.create(
        user=request.user, title=data["title"], content=data["content"]
    )
    return JsonResponse({"status": "ok", "note_id": note.id})
