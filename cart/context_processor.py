from cart.models import Cart
# context processor is used to pass the context variable in all the templet without assigning individually we must add these in templet in settings.py 

def cart(request):
    cart_instance = Cart.objects.filter(user=request.user).first()  # Fetch the user's cart from the database
    return {'cart':cart(request)}

 

