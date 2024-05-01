from django import forms
from site_app.models import  *
from django.forms.widgets import *

class Produto_form (forms.ModelForm):
    class Meta:

        model = Produto
        fields = ['prod_name','prod_imgUrl','prod_price','prod_description','prod_categoria']
        labels = { 
                'prod_name':'Nome do produto', 
                'prod_imgUrl':'Url da imagem', 
                'prod_price':'Preço',
                'prod_description': 'Descrição',
                'prod_categoria': 'Categoria'
                }
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prod_name'].widget.attrs.update(
            {'placeholder':'Título de exibição',
            'class' : 'form-control mt-2'}
        )
        self.fields['prod_imgUrl'].widget.attrs.update(
            {'placeholder':'link da imagem ',
            'class' : 'form-control mt-2'}
        )
        self.fields['prod_price'].widget.attrs.update(
            {'placeholder':'Preço atual',
            'class' : 'form-control mt-2'}
        )
        self.fields['prod_description'].widget.attrs.update(
            {'placeholder':'Informe as principais caracteristicas do produto, separando as linhas por ";" ',
            'class' : 'form-control mt-2'}
        )
        self.fields['prod_categoria'].widget.attrs.update(
            {'placeholder':'Selecione a categoria ideal do seu produto ',
            'class' : 'form-control mt-2'}
        )
        

class SignUp_form (forms.ModelForm):
    class Meta:
        
        model = Usuario
        fields = ['user_firstName','user_lastName','user_email','user_password']
        labels = {
            'user_firstName': 'Seu primerio nome',
            'user_lastName': "Seu sobrenome",
            'user_password': 'Senha',
            'user_email': 'E-mail'
        }
        widgets = {'user_password':PasswordInput()}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_firstName'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        )
        self.fields['user_lastName'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        )
        self.fields['user_password'].widget.attrs.update(
            {'placeholder':'Sua melhor senha',
            'class' : 'form-control mt-2'}
        )
        self.fields['user_email'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        )
        

class SignIn_form (forms.ModelForm):
    class Meta:
        
        model = Usuario
        fields = ['user_email','user_password']
        labels = {
            'user_email': 'Seu e-mail',
            'user_password': 'Senha',
        }
        widgets = {'user_password':PasswordInput()}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_password'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        )
        self.fields['user_email'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        )
        
class Influencer_form (forms.ModelForm):
    class Meta:
        
        model = Influencer
        
        fields = ['inf_name','inf_at','inf_store_name','produtos']
        labels = {
            'inf_name': 'Nome/Apelido como Influencer',
            'inf_at': 'Seu arroba',
            'inf_store_name': 'Nome da loja',
            'produtos': '',
        }
        # widgets = {'produtos': SelectMultiple()}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inf_name'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        )
        self.fields['inf_at'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        )
        self.fields['inf_store_name'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        ) 
        self.fields['produtos'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control mt-2'}
        )
        
class Catagoria_form (forms.ModelForm):
    class Meta:
        
        model = Categoria
        fields = ['cat_name']
        labels = {
            'cat_name': 'Categoria',
        }
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat_name'].widget.attrs.update(
            {'placeholder':'Nome da categoria',
            'class' : 'form-control mt-2'}
        )
     
  