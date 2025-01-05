from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
import uuid
import requests
from django.db import transaction

# Create your views here.

def place_order(request):
    cart=request.session.get('cart',[])
    total=0
    if not cart:
        messages.info(request,"No any item in cart")
        return redirect("/buy_product_list")
    for item in cart:
        total+=item['price']


   
    for item in cart:
           payment_id=str(uuid.uuid4())
           order.objects.create(
            name=item['name'],
            payment_id=payment_id,
            status='pending',
            total_amt=total,
            )
    request.session['cart']=[]    # after storing  the session data and creating the object clearing the session data replacing with list
    
    esewa_payment_url = "https://uat.esewa.com.np/epay/main" # these url is not applicable  yo chai just for testing transaction huncha ke nai 
    success_url = request.build_absolute_uri('payment_success/')  # Success URL
    failure_url = request.build_absolute_uri('payment_failure/')  # Failure URL
    params={
        'amt':total,
        'pdc':0, #product delivery charge,
        'psc':0, #product service charge
        'txAmt':0, 
        'tAmt':total,
        'scd':'EPAYTEST',
        'pid':payment_id, # payment id  is used to itentify the transcation by the uniques id 
        'su':success_url, # if success esewa will redirect to these page 
        'fu':failure_url  # if failure the esewa will redirect to these page 


    }
    return redirect(f"{esewa_payment_url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}")

# for validating the transaction
def validating_transaction(payment_id,amount):
    esewa_url="https://esewa.com.np/epay/transrec"
    data={
        'amt':amount,
        'pid':payment_id,
        'scd': 'EPAYTEST'# left ot provide the esewa merchant code 
    }
    responce=requests.post(esewa_url,data=data) # calling the api of esewa for validatiing the transaction is tranc=saction is validate the  it will send the success else not 

    if  responce.status_code==200 and 'SUCCESS' in responce.text: # checking if the responce is success or not 
        return  True
    else:
        return False

def payment_success(request):
    payment_id = request.GET.get('oid')  # get function  used  whent eh api of the esewa return the oid and amt after validating the transaction
    amount = request.GET.get('amt')

   
    if not payment_id or not amount:
        messages.error(request, "Payment ID or amount is missing.")
        return redirect('/buy_product_list/')
    
    
    is_valid = validating_transaction(payment_id, amount)
    
    if is_valid:
        try:
            
            orders = order.objects.filter(payment_id=payment_id)
            
            
            if not orders.exists():
                messages.error(request, "Invalid payment ID.")
                return redirect('/buy_product_list/')
            
          
            with transaction.atomic():  # Ensure atomicity of the operation
                for order in orders:
                    order.is_paid = True
                    order.status = 'paid'
                    order.save()  
                  

            messages.success(request, "Payment was successful.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}") 
        return redirect('/buy_product_list/')
    else:
        messages.error(request, "Payment is not validated.")
        return redirect('/buy_product_list/')


def payment_failure(request):
    messages.info(request,'payment_faild')
    return redirect('buy_product_list')

