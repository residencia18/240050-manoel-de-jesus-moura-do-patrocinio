from django.db import models

# Create your models here.

class produto (models.Model):
    prod_name = models.CharField(max_length=200)
    prod_imgUrl = models.CharField(max_length=200)
    prod_price = models.DecimalField(max_digits = 6, decimal_places=2)
    prod_description = models.TextField()
    createAt = models.DateTimeField(auto_now_add=False)
    
    def __str__ (self):
        return self.prod_name
