from django.db import models

# Create your models here.
class items(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    file=models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return self.name
    

