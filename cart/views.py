from django.shortcuts import render
from cart.models import *

# Create your views here.
def cart_summary(request):
    art_instance = Cart.objects.filter(user=request.user).first()
    return render(request, "cart_summary.html")


def cart_add(request):
    pass
def cart_delete(request):
    pass
def cart_update(request):
    pass 

