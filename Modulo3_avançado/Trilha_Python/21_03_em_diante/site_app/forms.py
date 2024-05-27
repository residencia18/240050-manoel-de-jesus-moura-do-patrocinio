from django import forms
from site_app.models import  *
from django.forms.widgets import *
from django.contrib.auth.models import User,Group


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
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['prod_imgUrl'].widget.attrs.update(
            {'placeholder':'link da imagem ',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['prod_price'].widget.attrs.update(
            {'placeholder':'Preço atual',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['prod_description'].widget.attrs.update(
            {'placeholder':'Informe as principais caracteristicas do produto, separando as linhas por ";" ',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['prod_categoria'].widget.attrs.update(
            {'placeholder':'Selecione a categoria ideal do seu produto ',
            'class' : 'form-control  w-100 rounded'}
        )
        

class SignUp_form (forms.ModelForm):
    class Meta:
        
        model = Usuario
        fields = ['username','last_name','cpf','dt_nascimento','email','password']
        labels = {
            'username': 'Seu primerio nome',
            'last_name': 'Seu sobrenome',
            'cpf': 'Seu CPF',
            'dt_nascimento': 'Data de aniversário',
            'email': 'E-mail',
            'password': 'Senha',
        }
        widgets = {
            'password':PasswordInput(),
             'dt_nascimento': DateInput(attrs={'type': 'date'}),
        }
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['cpf'].widget.attrs.update(
            {'placeholder':'XXX.XXX.XXX-XX',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['dt_nascimento'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control  w-100 rounded'}
        )
        
        self.fields['email'].widget.attrs.update(
            {'placeholder':'exemplo@gmail.com',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder':'Sua melhor senha',
            'class' : 'form-control  w-100 rounded'}
        )
        

class SignIn_form (forms.ModelForm):
    class Meta:
        
        model = User
        fields = ['username','password']
        labels = {
            'username': 'Usuario',
            'password': 'Senha',
        }
        widgets = {'password':PasswordInput()}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':'Seu nome de usuário',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control  w-100 rounded'}
        )
        
class Influencer_form (forms.ModelForm):
    class Meta:
        
        model = Influencer
        
        fields = ['inf_name','inf_at','inf_store_name']
        labels = {
            'inf_name': 'Nome/Apelido como Influencer',
            'inf_at': 'Seu arroba',
            'inf_store_name': 'Nome da loja',
        }
        # widgets = {'produtos': SelectMultiple()}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inf_name'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['inf_at'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control  w-100 rounded'}
        )
        self.fields['inf_store_name'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'form-control  w-100 rounded'}
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
            'class' : 'form-control  w-100 rounded'}
        )
     
        
class Search_form (forms.ModelForm):
    class Meta:
        
        model = Produto
        fields = ['prod_name']
        labels = {
            'prod_name': '',
        }
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prod_name'].widget.attrs.update(
            {'placeholder':'Qual peça você deseja ?',
            'class' : 'form-control  w-100 me-2 bg-white text-black rounded'}
        )

class Grupo_form (forms.ModelForm):
    class Meta:
        
        model = Group
        fields = ['name']
        labels = {
            'cat_name': 'Categoria',
        }
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder':'informe o nome do grupo ',
            'class' : 'form-control  w-100 rounded'}
        )
     
 