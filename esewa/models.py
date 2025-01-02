from django.db import models
from main.models import *


# Create your models here.
class order(models.Model):
    name=models.CharField(max_length=100)
    order_id=models.CharField(max_length=100)
    is_paid=models.BooleanField(default=False)
    total_amt=models.IntegerField()

    def __str__(self):
        return self.name
    



    