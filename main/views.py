from django.shortcuts import render
from login.views import *
from django.contrib.auth.decorators import login_required
from main.models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
@login_required(login_url="login_page")
def after_login(request):
    return render(request,"after_login.html")

def adding_item(request):
    if request.method=="POST":
       name=request.POST.get("name")
       price=request.POST.get("price")
       file=request.FILES.get("file")
       items.objects.create(
        name=name,
        price=price,
        file=file,
       ) 
       return redirect('/adding_item/')
    
    querryset=items.objects.all()# left search feature
    context={'items':querryset}
    return render(request,"adding_item.html",context)

def buy_product_list(request):
    
    
    querryset=items.objects.all()
    if request.GET.get('search'):# recomendation of search 
        querryset=querryset.filter(name__icontains =request.GET.get('search'))
    context={'items':querryset}
    
    return render(request,"buy_product_list.html",context)

#def buy(request,id):
    item=get_object_or_404(id=id)

    