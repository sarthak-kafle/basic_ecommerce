from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
def place_order(request):
    cart=request.session.get('cart',[])
    total=0
    if(cart==[]):
        messages.info(request,"No any item in cart")
    else:
        for item  in cart:
            
            total+=item['price']
            user=order.objects.create(
                name=item['name'],
                   
            )
            user.total_amt=total
            user.save()
            querryset=order.objects.all()
            context={'order':querryset}

            cart.clear() # after order is place clearing the cart data   
       
    return render(request,"place_order.html",context)

