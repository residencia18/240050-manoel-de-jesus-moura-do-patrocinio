from django.shortcuts import render
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from senhas_app.forms import UserForm
from django.contrib.auth.hashers import make_password
from senhas_app.models import Usuario
from django.contrib.auth.models import Permission, Group

def context (request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user_ptr_id=request.user.id)
        request.user.matricula = usuario.matricula
        request.user.cpf = usuario.cpf
        request.user.local = usuario.local
        request.user.cargo = usuario.cargo
        return {
            'formperfil':UserForm(instance=usuario),        #perfil
        }
    else:
        return {
            'formuser':UserForm(),                          #login
        }

def index (request):
    contexto = context(request)
    return render(request,'index.html',contexto)

def login (request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user:
            auth_login(request,user)
    return HttpResponseRedirect(reverse('index'))

def logout (request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def encerrar (request):
    usuario = Usuario.objects.get(user_ptr_id=request.user.id)
    usuario.is_active=False
    usuario.save()
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def editarperfil (request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(user_ptr_id=request.user.id)
        novo_usuario = request.POST.copy()
        novo_usuario['username'] = usuario.username
        novo_usuario['password'] = usuario.password
        form = UserForm(instance=usuario, data=novo_usuario)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('index'))

'''
    Funções de superusuario
'''

def caduser (request):
    if request.method == 'POST' and request.user.is_superuser:
        user = UserForm(request.POST)
        if user.is_valid():
            if user.data.get('password') != user.data.get('confirmacao'):
                user.add_error('password','A senha e confirmação devem ser iguais')
            else:
                permlist = []
                for permissao in request.POST.getlist("permissao"):
                    permlist.append(Permission.objects.get(id=permissao))

                user = user.save(commit=False)
                user.password = make_password(user.password)
                user.save()

                user.user_permissions.set(permlist)
        return HttpResponseRedirect(reverse('painel'))
    return HttpResponseRedirect(reverse('index'))

def toggleactive (request,id):
    if request.method == 'GET' and request.user.is_superuser:
        usuario = Usuario.objects.get(user_ptr_id=id)
        usuario.is_active = not usuario.is_active
        usuario.save()
        return HttpResponseRedirect(reverse('painel'))
    return HttpResponseRedirect(reverse('index'))

def painel (request):
    if request.method == 'GET' and request.user.is_superuser:
        permissoes = Permission.objects.order_by('id')
        permissoes_agrupadas = {}
        for permissao in permissoes:
            objeto = permissao.codename.split("_")
            if objeto[1] not in permissoes_agrupadas:
                permissoes_agrupadas[objeto[1]] = {objeto[0] : permissao.id}
            else:
                permissoes_agrupadas[objeto[1]][objeto[0]] = permissao.id
        contexto = context(request)
        contexto['formuser'] = UserForm()
        contexto['permissoes'] = permissoes_agrupadas
        contexto['grupos'] = Group.objects.all()
        contexto['users'] = Usuario.objects.order_by('first_name')
        return render(request,'painel.html',contexto)
    return HttpResponseRedirect(reverse('index'))
