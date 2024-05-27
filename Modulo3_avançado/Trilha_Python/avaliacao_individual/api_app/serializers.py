from rest_framework import serializers
from site_app.models import *

class ProdutoSerializers (serializers.ModelSerializer):
  class Meta: 
    model = Produto
    fields = ['id','nome','descricao','valor','limite_cri','limite_adu','limite_bebe','limite_animal','tipo']
  
class RelacaoSerializers (serializers.ModelSerializer):
  class Meta: 
    model = Relacao
    fields = ['id','inicio','fim','qtd_crianca','fk_produto','fk_usuario','fk_nivel']


class AuxiliarSerializers (serializers.ModelSerializer):
  class Meta: 
    model = Auxiliar
    fields = ['id','fk_produto','fk_tag']
  