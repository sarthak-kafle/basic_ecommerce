from django.shortcuts import render
from login.views import *
from django.contrib.auth.decorators import login_required
from main.models import *

# Create your views here.
@login_required(login_url="login_page")
def after_login(request):
    return render(request,"after_login.html")
def adding_item(request):
    if request.method=="POST":
       name=request.POST.get("name")
       price=request.POST.get("price")
       file=request.POST.FILE.get("file")
       items.objects.create(
        name=name,
        price=price,
        file=file,
       ) 
       return redirect('/adding_item/')
    
    querryset=items.objects.all()# left search feature
    context={'items':querryset}
    return render("adding_item.html",context)


