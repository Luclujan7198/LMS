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
    ra = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=80)
    celular = models.CharField(max_length=11)
    sigla_curso = models.CharField(max_length=10)

    def __str__(self):
        return str(self.ra)

    class Meta():
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class GradeCurricular(models.Model):
    curso = models.OneToOneField(Curso, default=True)
    ano = models.IntegerField(unique=True)
    semestre = models.CharField(max_length=1, unique=True)
    class Meta():
        verbose_name = 'Grade Curricular'
        verbose_name_plural = 'Grades Curriculares'

    def __str__(self):
        return self.curso.nome

class Periodo(models.Model):
    cursos = models.OneToOneField(Curso)
    numero = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.cursos.nome