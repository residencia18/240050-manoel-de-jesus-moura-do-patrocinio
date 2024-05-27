from rest_framework import serializers
from site_app.models import *

class GetRoupasSerializers (serializers.ModelSerializer):
  class Meta: 
    model = Produto
    fields = ['id','prod_name','prod_imgUrl','prod_price','prod_description','prod_categoria']
  