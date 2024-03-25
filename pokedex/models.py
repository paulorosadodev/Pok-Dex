from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nome = models.CharField(max_length=50)
    tipo1 = models.CharField(max_length=50)
    tipo2 = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
