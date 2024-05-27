from django.db import models
from django.contrib.auth.models import User

class Cargo (models.Model):
    nome = models.TextField()
    class Meta:
        verbose_name_plural = 'Cargos'
    def __str__ (self):
        return self.nome

class Usuario (User):
    cpf = models.TextField(null=True)
    matricula = models.TextField(null=True)
    local = models.ForeignKey('Local',on_delete=models.CASCADE)
    cargo = models.ForeignKey('Cargo',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Usuarios'
    def __str__ (self):
        return self.first_name + self.last_name 

class Local (models.Model):
    nome = models.TextField()
    class Meta:
        verbose_name_plural = 'Locais'
    def __str__ (self):
        return self.nome

class Chamada (models.Model):
    nome = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    local = models.ForeignKey('Local',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Senhas'
    def __str__ (self):
        return self.nome