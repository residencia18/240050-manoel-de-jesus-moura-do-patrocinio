from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Produto (User):
    
    title = models.CharField(max_length=200)
    prod_price = models.DecimalField(max_digits = 6, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    # prod_categoria =  models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    
    
    def _str_ (self):
        return self.prod_name
    
class Usuarios (User):
    birthday = models.DateTimeField(auto_now_add=True)

