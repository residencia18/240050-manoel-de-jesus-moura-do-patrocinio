from django.shortcuts import render

from taygra_app.forms import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout as authLogout
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password


def home (request): 
    return render(request,'home.html')

def page_login (request): 
    if request.method == "POST":
        form = Login_form(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else: 
            form.add_error(None, "Credenciais inválidas. Por favor, tente novamente.")
    else:
        form = Login_form()
        
    context = {'form_signIn':form}
    return render(request,'login.html',context)

def page_logout(request):
    authLogout(request)
    return HttpResponseRedirect(reverse('home'))
 
def page_registro (request): 
    if request.method == "POST":
        form = cadastro_form(request.POST)
        if form.is_valid():
            if request.POST.get('id_user_confirme_password') != request.POST.get('password'):
              form.add_error("password","As senha precisam ser iguais")  
            else:
                post = form.save(commit=False)
                post.password = make_password(post.password)
                post.save()
                return HttpResponseRedirect(reverse('home'))
    else:
        form = cadastro_form()
        
    context = {'form_signUp':form}
    return render(request,'registro.html',context)

# auth pages


def page_editperfil (request):
    if request.method == 'POST':
        usuario = User.objects.get(id=request.user.id)
        novo_usuario = request.POST.copy()
        
        novo_usuario['password'] = make_password(request.POST["password"])
        novo_usuario['username'] = usuario.username
        
        print("request.POST",request.POST["password"])
        user = cadastro_form(instance=usuario, data=novo_usuario)
        if user.is_valid:
            user.save()
            return HttpResponseRedirect(reverse('home'))
    else:        
        if request.user.is_authenticated:
            context = {
                'formEdit' : cadastro_form(),
            }
            context['formEdit'] = cadastro_form(instance=User.objects.get(id=request.user.id))
            return render(request,"edit_user.html",context) 
        else:
            return HttpResponseRedirect(reverse('home'))

def deleteUser (request, id):
    user = User.objects.get(id=id)
    user.delete()
    authLogout(request)
    return HttpResponseRedirect(reverse('home'))
