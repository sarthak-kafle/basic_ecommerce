from django.shortcuts import render
from login.views import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login_page")
def after_login(request):
    pass
    return render(request,"after_login.html")