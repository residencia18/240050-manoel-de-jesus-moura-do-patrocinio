from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User


class Login_form (forms.ModelForm):
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
            'class' : 'w-100 form-control mt-2'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'w-100 form-control mt-2'}
        )
     
class cadastro_form (forms.ModelForm):
    class Meta:
        
        model = User
        fields = ['username','last_name','email','password']
        labels = {
            'username': 'Seu primerio nome',
            'last_name': "Seu sobrenome",
            'email': 'E-mail',
            'password': 'Senha',
        }
        widgets = {'password':PasswordInput()}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'w-100 form-control mt-2'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'w-100 form-control mt-2'}
        )
        
        self.fields['email'].widget.attrs.update(
            {'placeholder':'',
            'class' : 'w-100 form-control mt-2'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder':'Sua melhor senha',
            'class' : 'w-100 form-control mt-2'}
        )
        
