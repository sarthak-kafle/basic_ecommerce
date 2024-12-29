from django.shortcuts import render,redirect
from cart.models import *
from main.models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def cart_summary(request,id):
    

    try:
      user=items.objects.get(id=id)
    except :
     messages.info(request,"item not found")
     return redirect("/buy_product_list/")
    cart=request.session.get("cart",[])#cart is used for geting the sesson deta of cart and empty dict is used if there is no any value of cart it will not rais erroe for that purpose []is used bu dict can alos be used 
    cart.append(
       {
              "name":user.name,
              "price":user.price,
       }

     )
    request.session['cart']=cart
    return redirect("/buy_product_list/")
def view_cart(request):
   cart=request.session.get('cart',[])
   total=0
   for item in cart:
        total+=item['price']

   context={
      "cart":cart,
      "total":total
   }


   return render(request,"view_cart.html",context)


def cart_add(request):
    pass
def cart_delete(request):
    pass
def cart_update(request):
    pass 

