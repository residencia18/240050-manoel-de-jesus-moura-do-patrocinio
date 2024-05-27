from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from site_app.models import *
from api_app.serializers import *

# Create your views here.

@api_view(['GET','POST'])
def produtos(request):
  if request.method == "POST" and request.user.is_authenticated and "site_app" in request.user.get_all_permition:
    serializer = ProdutoSerializers(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status= status.HTTP_201_CREATED)
 
    return Response(serializer.erros,status= status.HTTP_400_BAD_REQUEST)
       
  elif request.method == "GET":
    produtoData = Produto.objects.order_by('id') 
    serializer = ProdutoSerializers(produtoData,many=True) 
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def produto_id(request, produto_id):
  try:
    produtoData = Produto.objects.get(id=produto_id) 
  except Produto.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if  request.method == "GET":
    serializer = ProdutoSerializers(produtoData)
    return Response(serializer.data,status= status.HTTP_200_OK)
    
  elif  request.method == "PUT":
    serializer = ProdutoSerializers(instance=produtoData, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status= status.HTTP_202_ACCEPTED)
    
    return Response(serializer.erros,status= status.HTTP_400_BAD_REQUEST)

  else :
    produtoData.delete()
    return Response(status= status.HTTP_200_OK)
    

@api_view(['GET','POST'])
def relacoes(request):
  if request.method == "POST" and request.user.is_authenticated :
    serializer = RelacaoSerializers(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status= status.HTTP_201_CREATED)
 
    return Response(serializer.erros,status= status.HTTP_400_BAD_REQUEST)
       
  elif request.method == "GET":
    relacoesData = Relacao.objects.order_by('id') 
    serializer = RelacaoSerializers(relacoesData,many=True) 
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def relacao_id(request, relacao_id):
  try:
    relacoesData = Relacao.objects.get(id=relacao_id) 
  except Relacao.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if  request.method == "GET":
    serializer = RelacaoSerializers(relacoesData)
    return Response(serializer.data,status= status.HTTP_200_OK)
    
  elif  request.method == "PUT" and request.user.is_authenticated :
    serializer = RelacaoSerializers(instance=relacoesData, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status= status.HTTP_202_ACCEPTED)
    
    return Response(serializer.erros,status= status.HTTP_400_BAD_REQUEST)

  elif request.method == "DELETE" and request.user.is_authenticated :
    relacoesData.delete()
    return Response(status= status.HTTP_200_OK)
 