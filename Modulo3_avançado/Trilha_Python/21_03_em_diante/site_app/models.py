from django.db import models
from django.contrib.auth.models import User
import datetime

class Categoria (models.Model):
    cat_name = models.CharField(max_length=15)

    def __str__ (self):
        return self.cat_name
 
class Usuario (User):
    cpf = models.CharField(max_length=14)
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento")

    class Meta:
        verbose_name_plural = 'Usuarios'
    def __str__ (self):
        return self.username

 
class Produto (models.Model):
    
    prod_name = models.CharField(max_length=200)
    prod_imgUrl = models.CharField(max_length=200)
    prod_price = models.DecimalField(max_digits = 6, decimal_places=2)
    prod_description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    prod_categoria =  models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    
    
    def __str__ (self):
        return self.prod_name

class Influencer (models.Model):
    inf_name = models.CharField(max_length=200)
    inf_at = models.CharField(max_length=70)
    inf_store_name = models.CharField(max_length=200)
    mainColor = models.CharField(max_length=15, default="Orange")
    produtos = models.ManyToManyField(Produto)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.inf_name

class Venda (models.Model):
    
    vend_total = models.DecimalField(max_digits = 6, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    vend_cliente =  models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__ (self):
        return self.vend_total
     
class ProdutosVenda(models.Model):
    product = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    influencers =  models.ForeignKey(Influencer,on_delete=models.CASCADE,null=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.product.prod_name} - {self.influencer.inf_name}"

class ProdutoInfluencer(models.Model):
    product = models.ForeignKey(Produto, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.prod_name} - {self.influencer.inf_name}"


# MODELS DA AVALIAÇÃO INDIVIDUAL


class Tipo (models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return self.nome

class Tag (models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return self.nome
    
class Nivel (models.Model):
    nome = models.CharField(max_length=100)

    def __str__ (self):
        return self.nome


class Produto2 (models.Model):
    
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits = 6, decimal_places=2)
    limite_cri = models.IntegerField(null=True)
    limite_adu = models.IntegerField(null=True)
    limite_bebe =   models.IntegerField(null=True)
    limite_animal =  models.IntegerField(null=True)
    tipo =  models.ForeignKey(Tipo,on_delete=models.CASCADE,null=True)
    
    def __str__ (self):
        return self.nome

   

class Relacao(models.Model):
    inicio = models.DateField(verbose_name="Data de inicio")
    fim = models.DateField(verbose_name="Data de saida")
    qtd_crianca =  models.IntegerField(null=True)
    
    fk_produto = models.ForeignKey(Produto2, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.inicio} - {self.fim}"


class Auxiliar(models.Model):
    fk_produto = models.ForeignKey(Produto2, on_delete=models.CASCADE)
    fk_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
