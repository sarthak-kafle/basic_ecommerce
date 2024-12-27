from django.shortcuts import render
from cart.models import *
from main.models import *
from django.contrib import messages

# Create your views here.
def cart_summary(request,id):
    

    try:
      user=items.objects.get(id=id)
    except :
     messages.info(request,"item not found")
        
    context={
        'users':user,
    }    
    
    return render(request, "cart_summary.html",context)


def cart_add(request):
    pass
def cart_delete(request):
    pass
def cart_update(request):
    pass 

