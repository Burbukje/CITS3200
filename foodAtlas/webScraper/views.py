from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("uploader")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


def uploader(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        return render(request, "uploader.html")