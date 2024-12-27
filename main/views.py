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
    search_query=request.GET.get('search')
    if  search_query:# recomendation of search 
        querryset=querryset.filter(name__icontains =request.GET.get('search'))
    context={'items':querryset}
    
    return render(request,"buy_product_list.html",context)

def delete_item(request,id):
    try:
      queryset=items.objects.get(id=id)
      queryset.delete()
    except :
        print("exceptation raise")
    return redirect('adding_item')

def update(request,id):
    queryset=items.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        price=request.POST.get("price")
        file=request.FILES.get("file")


        queryset.name=name
        queryset.price=price
        if file:
            queryset.file=file

        queryset.save()
        return redirect('adding_item')
    return render (request,'update.html')




    