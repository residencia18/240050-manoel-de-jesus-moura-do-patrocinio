from senhas_app.models import Usuario
from django import forms
from django.forms.widgets import *

class UserForm (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','password','first_name','last_name','email','cpf','matricula','cargo','local']
        widgets = {'password': PasswordInput(),'cpf':TextInput(),'matricula':TextInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].widget.attrs.update({'required':'True','placeholder':'Login','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['password'].widget.attrs.update({'required':'True','placeholder':'Senha','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['first_name'].widget.attrs.update({'required':'True','placeholder':'Nome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['last_name'].widget.attrs.update({'required':'True','placeholder':'Sobrenome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['email'].widget.attrs.update({'required':'True','placeholder':'Email','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['cpf'].widget.attrs.update({'required':'True','placeholder':'CPF','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['matricula'].widget.attrs.update({'required':'True','placeholder':'Matrícula','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['cargo'].widget.attrs.update({'required':'True','class':'col form-control my-2 p-2'})
        self.fields['local'].widget.attrs.update({'required':'True','class':'col form-control my-2 p-2'})
