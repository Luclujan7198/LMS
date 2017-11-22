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
    nome = models.CharField(max_length=240, unique=True, default='')
    carga_horaria = models.IntegerField()
    teoria = models.DecimalField(decimal_places=3, max_digits=3)
    pratica = models.DecimalField(decimal_places=3, max_digits=3) 
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_basica = models.TextField()
    bibliografica_complementar = models.TextField()

    def __str__(self):
        return self.nome
    
class DisciplinaOfertada(models.Model):
    id_disciplina_ofertada = models.AutoField(primary_key=True)
    nome_disciplina = models.OneToOneField(Disciplina,default='')
    ano = models.IntegerField(unique=True)
    semestre = models.CharField(unique=True, max_length=1)
    #fk_disciplina = models.ForeignKey(Disciplina)
 
    def __str__(self):
        return self.nome_disciplina.nome

class Turma(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina)
    ano_ofertado = models.OneToOneField(DisciplinaOfertada)
    id_turma = models.AutoField(primary_key=True)
    turno = models.CharField(max_length=15)
    #ra_professor = models.ForeignKey(unique=True, Professor)

    def __str__(self):
        return self.nome_disciplina.nome 

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