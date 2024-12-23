from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from login.models import *
from django.contrib.auth.hashers import make_password

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is already taken.")
            return redirect("/register/") 

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request,"registred successfully!")
        return redirect('login_page')

    return render(request, "register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Username does not exist.")
            return redirect("/login_page/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid password. Please try again.")
            return redirect("/login_page/")
        else:
            login(request, user)
            return redirect("/after_login/")

    return render(request, 'login_page.html')