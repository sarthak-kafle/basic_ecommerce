from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
import uuid
import requests

# Create your views here.

def place_order(request):
    cart=request.session.get('cart',[])
    total=0
    if not cart:
        messages.info(request,"No any item in cart")
        return redirect("/buy_product_list")
    for item in cart:
        total+=item['price']

    payment_id=str(uuid.uuid4()) # these is used for creating the different payment id for the every order  
    for item in cart:
        order.objects.create(
            name=item['name'],
            payment_id=payment_id,
            status='pending',
            total_amt=total,
        )
    request.session['cart']=[] # after storing  the session data and creating the object clearing the session data replacing with list
    
    esewa_payment_url = "https://esewa.com.np/epay/main"
    success_url = request.build_absolute_uri('/payment-success/')  # Success URL
    failure_url = request.build_absolute_uri('/payment-failure/')  # Failure URL
    params={
        'amt':total,
        'pdc':0, #product delivery charge,
        'psc':0, #product service charge
        'taxamt':0, 
        'tamt':total,
        'pid':payment_id, # payment id  is used to itentify the transcation by the uniques id 
        'su':success_url,
        'fu':failure_url


    }
    return redirect(f"{esewa_payment_url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}")

# for validating the transaction
def validating_transaction(payment_id,amount):
    merchant_code=0
    esewa_url="https://esewa.com.np/epay/transrec"
    data={
        'amt':amount,
        'pid':payment_id,
        'scd': merchant_code# left ot provide the esewa merchant code 
    }
    responce=requests.post(esewa_url,data=data) # calling the api of esewa for validatiing the transaction is tranc=saction is validate the  it will send the success else not 
    
    if  responce.txt=='success':
        return  True
    else:
        return False
    
    




def payment_success(request,payment_id):
    try:
        user=order.objects.get(payment_id=payment_id)
    except:
        messages.info(request,'payment_id is not matching with the save one in the data base ')
        return redirect('/buy_product_list/')
    if not user :
        messages.info(request,'payment fiald payment id not matching')
    else:
        user.is_paid=True
        user.status='paid'
        user.save()
        messages.info(request,'payment success')
    return redirect('/buy_product_list/')

def payment_failure(request):
    messages.info(request,'payment_faild')
    return redirect('buy_product_list')

