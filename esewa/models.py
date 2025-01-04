from django.db import models
from main.models import *


# Create your models here.
class order(models.Model):
    name=models.CharField(max_length=100)
    payment_id=models.CharField(maxlength=100,unique=True)
    is_paid=models.BooleanField(default=False)
    total_amt=models.IntegerField()
    status=models.CharField(max_length=40,default='pending')

    def __str__(self):
        return self.name
    



    