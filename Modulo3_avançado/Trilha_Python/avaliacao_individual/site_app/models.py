from django.db import models
from django.contrib.auth.models import User

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

class Usuario (User):
    cpf = models.CharField(max_length=14)
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento")

    class Meta:
        verbose_name_plural = 'Usuarios'
    def __str__ (self):
        return self.username
 
 
class Produto (models.Model):
    
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
    
    fk_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.inicio} - {self.fim}"

class Auxiliar(models.Model):
    fk_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fk_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
