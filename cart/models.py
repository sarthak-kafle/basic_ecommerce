from django.db import models

# Create your models here
class cart_item(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=100,decimal_places=3)
    session_key=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

