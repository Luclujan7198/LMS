from django.db import models

# Create your models here.


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=10, default='')
    nome = models.CharField(unique=True, max_length=200)


    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True) 
    carga_horaria = models.IntegerField()
    teoria = models.DecimalField(decimal_places=3, max_digits=3)
    pratica = models.DecimalField(decimal_places=3, max_digits=3) 
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_basica = models.TextField()
    bibliografica_complementar = models.TextField()
    
class DisciplinaOfertada(models.Model):
    id_disciplina_ofertada = models.AutoField(primary_key=True)
    ano = models.SmallIntegerField(unique=True)
    semestre = models.CharField(unique=True, max_length=1)
    fk_disciplina = models.ForeignKey(Disciplina)


