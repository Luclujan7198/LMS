from django.db import models

# Create your models here.

class Curso(models.Model):
    sigla = models.CharField(max_length=10, default='')
    nome = models.CharField(max_length=200)
    matutino = models.BooleanField(default=False)
    vespertino = models.BooleanField(default=False)
    noturno = models.BooleanField(default=False)
    integral = models.BooleanField(default=False)
    modalidade = models.CharField(max_length=200)
    duracao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Alunos(models.Model):
    ra = models.IntegerField(max_length=10 default=True)
    nome = models.CharField(max_length=200 default=True)
    email = models.CharField(max_length=80 default=True)
    celular = models.IntegerField(max_length=20 default=True)
    sigla_curso = models.CharField(max_length=10 default=True)

    def __str__(self):
        return self.nome