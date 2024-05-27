from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from site_app.models import *
from api_app.serializers import *

# Create your views here.

@api_view(['GET','POST'])
def roupas(request):
  if request.method == "POST" and request.user.is_authenticated and "site_app" in request.user.get_all_permition:
    serializer = GetRoupasSerializers(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status= status.HTTP_201_CREATED)
 
    return Response(serializer.erros,status= status.HTTP_400_BAD_REQUEST)
       
  elif request.method == "GET":
    produtoData = Produto.objects.order_by('id') 
    serializer = GetRoupasSerializers(produtoData,many=True) 
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def roupas_id(request, produto_id):
  try:
    produtoData = Produto.objects.get(id=produto_id) 
  except Produto.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if  request.method == "GET":
    serializer = GetRoupasSerializers(produtoData)
    return Response(serializer.data,status= status.HTTP_200_OK)
    
  elif  request.method == "PUT":
    serializer = GetRoupasSerializers(instance=produtoData, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status= status.HTTP_202_ACCEPTED)
    
    return Response(serializer.erros,status= status.HTTP_400_BAD_REQUEST)

  else :
    produtoData.delete()
    return Response(status= status.HTTP_200_OK)
    