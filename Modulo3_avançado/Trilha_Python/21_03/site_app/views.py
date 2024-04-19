from django.shortcuts import render
from site_app.models import Produto
from site_app.forms import produto_form
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home (request): 
    produtoData = Produto.objects.order_by('id')
    context = {'produtos': produtoData} 
    return render(request,'home.html',context)

def page_roupas (request):
    produtoData = Produto.objects.order_by('id')
    context = {'produtos': produtoData} 
    return render(request,'roupas.html',context)

def page_roupa_detalhe(request, produto_id):
    produtoData = Produto.objects.get(id=produto_id)
    context = {'produto':produtoData}
    return render(request,'roupa_detalhe.html',context)


def page_login (request): 
    return render(request,'login.html')

def page_registro (request): 
    
    return render(request,'registro.html')


# Admin views

def page_registroProduto (request): 
    if request.method == "POST":
        form = produto_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = produto_form()
        
    context = {'form_add':form}
    return render(request,'registroProduto.html',context)

