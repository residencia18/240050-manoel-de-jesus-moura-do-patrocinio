from django import forms
from site_app.models import  Produto
from django.http import HttpResponseRedirect
from django.urls import reverse

class produto_form (forms.ModelForm):
    class Meta:

        model = Produto
        fields = ['prod_name','prod_imgUrl','prod_price','prod_description']
        labels = {'Nome do produto': 'Url da imagem','Preço': 'Descrição'}
        
# class user_form (forms.ModelForm):
#     class Meta:

#         model = produto
#         fields = ['Username','password']
#         labels = {'Seu nome': 'Sua senha'}