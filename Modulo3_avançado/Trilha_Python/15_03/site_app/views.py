from django.shortcuts import render
from site_app.models import produto
# Create your views here.
def home (request): 
    produtoData = produto.objects.order_by('id')
    print(produtoData)
    context = {'produto': produtoData}
    return render(request,'home.html',context)


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})


def page_roupas (request):
    produtoData = produto.objects.order_by('id')
    context = {'produto': produtoData}
    return render(request,'roupas.html',context)

def page_prod_detail(request):
    pass
    # path('produto/<int:produto_id>/', detalhes_produto, name='detalhes_produto'),