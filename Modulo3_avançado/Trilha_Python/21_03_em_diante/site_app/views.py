from django.shortcuts import render
from site_app.models import *
from site_app.forms import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout as authLogout
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission, Group


def home (request): 
    form = Search_form()
    results = []
    if request.method == 'POST' :
        form = Search_form(request.POST)
        if form.is_valid():
            query = request.POST.get('prod_name')
            results = Produto.objects.filter(prod_name__icontains=query)
            
    produtoData = Produto.objects.order_by('id')        
    context = {'produtos': produtoData,'searchForm': form, 'results': results} 
    return render(request,'home.html',context)

def search(request):
    form = Search_form()
    results = []
    if request.method == 'POST' :
        form = Search_form(request.POST)
        if form.is_valid():
            query = request.POST.get('prod_name')
            results = Produto.objects.filter(prod_name__icontains=query)
            
    context = {'searchForm': form, 'results': results} 
    return render(request,'search_result.html',context)


def page_roupas (request):
    produtoData = Produto.objects.order_by('id')
    context = {'produtos': produtoData} 
    return render(request,'roupas.html',context)

def page_roupa_detalhe(request, produto_id):
    produtoData = Produto.objects.get(id=produto_id)
    context = {'produto':produtoData}
    return render(request,'roupa_detalhe.html',context)


def page_login (request): 
    if request.method == "POST":
        form = SignIn_form(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else: 
            form.add_error(None, "Credenciais inválidas. Por favor, tente novamente.")
    else:
        print("requisição do tipo get")
        form = SignIn_form()
        
    context = {'form_signIn':form}
    return render(request,'login.html',context)

def logout(request):
    authLogout(request)
    return HttpResponseRedirect(reverse('home'))
    
def page_registro (request): 
    if request.method == "POST":
        form = SignUp_form(request.POST)
        if form.is_valid():
            if request.POST.get('id_user_confirme_password') != request.POST.get('password'):
              form.add_error("password","As senha precisam ser iguais")  
            else:
                post = form.save(commit=False)
                post.password = make_password(post.password)
                post.save()
                
                return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUp_form()
        
    context = {'form_signUp':form}
    return render(request,'registro.html',context)

def page_registro_influencer (request): 
    if request.method == "POST":
        form = Influencer_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('registro_influencer'))
    else:
        form = Influencer_form()
        
    context = {'form_influencer':form}
    return render(request,'registro_influencer.html',context)

def removeAccount(request):

    if request.user.is_authenticated:
        try:
            userData = User.objects.get(id=request.user.id)
            userData.delete()
            authLogout(request)
        except User.DoesNotExist:
            # caso em que o usuário não existe
            return HttpResponseRedirect(reverse('home'))
            
    return HttpResponseRedirect(reverse('home'))
    
def page_about(request):
    return render(request,'sobre.html')

def page_editperfil (request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(user_ptr_id=request.user.id)
        novo_usuario = request.POST.copy()
        
        novo_usuario['password'] = usuario.password
        novo_usuario['username'] = usuario.username
        
        user = SignUp_form(instance=usuario, data=novo_usuario)
        if user.is_valid:
            user.save()
            return HttpResponseRedirect(reverse('home'))
    else:        
        if request.user.is_authenticated:
            context = {
                'formEdit' : SignUp_form(),
            }
            context['formEdit'] = SignUp_form(instance=Usuario.objects.get(user_ptr_id=request.user.id))
            return render(request,"edit_user.html",context) 
        else:
            return HttpResponseRedirect(reverse('home'))

# Admin views

def page_registroProduto (request): 
    if request.method == "POST":
        form = Produto_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('createProduct')
    else:
        form = Produto_form()
        
    context = {'form_add':form}
    return render(request,'registroProduto.html',context)

def page_registerCategory(request):
    if request.method == "POST":
        form = Catagoria_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('home'))           
    else:
        form = Catagoria_form()
        
    context = {'form_addCategoria':form}
    return render(request,'registro_categoria.html',context)

def toggleactive (request,user_id):
    if request.method == 'GET' and request.user.is_superuser:
        usuario = Usuario.objects.get(user_ptr_id=user_id)
        usuario.is_active = not usuario.is_active
        usuario.save()
        return HttpResponseRedirect(reverse('painel'))
    return HttpResponseRedirect(reverse('index'))

def page_group(request):
    if request.method == "POST" and request.user.is_authenticated and  request.user.is_superuser:
        form = Grupo_form(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return HttpResponseRedirect(reverse('addGroup'))
    else:
        form = Grupo_form()
        
    context = {'form_group':form}
    return render(request,'registro_group.html',context)

 
def page_admCadUser (request): 
    if request.method == "POST" and request.user.is_superuser:
        form = SignUp_form(request.POST)
        if form.is_valid():
            if request.POST.get('id_user_confirme_password') != request.POST.get('password'):
              form.add_error("password","As senha precisam ser iguais")  
            else:
                permlist = []
                grouplist = []
                for permissao in request.POST.getlist("permissao"):
                    permlist.append(Permission.objects.get(id=permissao))
                
                for group in request.POST.getlist("grupo"):
                    grouplist.append(Group.objects.get(id=group))

                post = form.save(commit=False)
                post.password = make_password(post.password)
                post.save()
                
                post.user_permissions.set(permlist)
                post.groups.set(grouplist)
                
        return HttpResponseRedirect(reverse('painel'))
    return render(request,'home.html')


def page_admEditUser (request,user_id): 
    if request.method == "POST" and request.user.is_superuser:
        print(" id recebido ", user_id)
        usuario = Usuario.objects.get(user_ptr_id=user_id)
        novo_usuario = request.POST.copy()
        
        novo_usuario['password'] = usuario.password
        novo_usuario['username'] = usuario.username
        
        form = SignUp_form(instance=usuario, data=novo_usuario)
        if form.is_valid:
            user = form.save()
            
            permlist = []
            grouplist = []
            for permissao in request.POST.getlist("permissao"):
                permlist.append(Permission.objects.get(id=permissao))
            
            for group in request.POST.getlist("grupo"):
                grouplist.append(Group.objects.get(id=group))
            
            user.user_permissions.set(permlist)
            user.groups.set(grouplist)
                
        return HttpResponseRedirect(reverse('painel'))
    return render(request,'home.html')
   
def page_painelAdmin(request):
    if request.method == 'GET' and request.user.is_superuser:
        permissoes = Permission.objects.order_by('id')
        permissoes_agrupadas = {}
        
        for permissao in permissoes:
            objeto = permissao.codename.split("_")
            if objeto[1] not in permissoes_agrupadas:
                permissoes_agrupadas[objeto[1]] = {objeto[0] : permissao.id}
            else:
                permissoes_agrupadas[objeto[1]][objeto[0]] = permissao.id
                
        contexto = {'formuser': SignUp_form()}
        contexto['permissoes'] = permissoes_agrupadas
        contexto['grupos'] = Group.objects.all()
        contexto['users'] = [(user.id, user, SignUp_form(instance=user, auto_id=False)) for user in Usuario.objects.order_by('first_name')]
        
        return render(request,'painel.html',contexto)
    return HttpResponseRedirect(reverse('home'))