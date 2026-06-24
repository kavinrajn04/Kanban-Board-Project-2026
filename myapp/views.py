from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
# myapp/views.py


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("sidebar")  # wherever you want to send them after login
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


def dashboard_view(request):
    return render(request, "dashboard.html", {"username": request.user.username})

