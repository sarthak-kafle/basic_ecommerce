from django.db import models

# Create your models here
class Cart:
    def __init__(self,request):
        self.session=request.session    # session_data=information stored about a user's activity during a specific period of time on a website or application
        # get the corrent sesson key
        cart=self.session.get('session_key')
        #if the user is new ,no session key
        if 'session_key'  not in request.session:
            create=self.session['session_key']={}
        
        #make sure cart is available all page of site
        self.cart=cart
