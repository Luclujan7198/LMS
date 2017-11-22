from django.db import models
from Auth.models import Professor, Aluno

class Curso(models.Model):
    sigla = models.CharField(max_length=10)
    nome = models.CharField(max_length=200)

    class Meta:
        unique_together = (('sigla', 'nome'),)

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
    disciplina = models.ForeignKey(Disciplina)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        unique_together = (('disciplina', 'ano', 'semestre'),)
    
    def __str__(self):
        return self.disciplina + ' - ' + str(self.ano) + ' - ' + self.semestre

class Turma(models.Model):
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada)
    id_turma = models.CharField(max_length=1)
    turno = models.CharField(max_length=15)
    professor = models.ForeignKey(Professor)

    class Meta:
        unique_together = (('disciplina_ofertada', 'id'),)

    def __str__(self):
        return self.disciplina_ofertada + ' - ' + self.id_turma

class GradeCurricular(models.Model):
    curso = models.ForeignKey(Curso)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=1)

    class Meta():
        unique_together = (('curso', 'ano', 'semestre'),)
        verbose_name = 'Grade Curricular'
        verbose_name_plural = 'Grades Curriculares'

    def __str__(self):
        return self.curso + ' - ' + str(self.ano) + ' - ' + self.semestre

class Periodo(models.Model):
    grade_curricular = models.ForeignKey(GradeCurricular)
    numero = models.IntegerField()

    class Meta:
        unique_together = (("grade_curricular", "numero"),)

    def __str__(self):
        return self.grade_curricular + ' - ' + str(self.numero)

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno)
    turma = models.ForeignKey(Turma)

    class Meta:
        unique_together = (('aluno', 'turma'),)

    def __str__(self):
        return self.aluno + ' - ' + self.turma

class Questao(models.Model):
    turma = models.ForeignKey(turma)
    numero = models.IntegerField()
    data_limite_entrega = models.DateField()
    descricao = models.TextField()
    data = models.DateField(auto_now=True)

    class Meta:
        unique_together = (('turma', 'numero'),)

    def __str__(self):
        return self.turma + ' - ' + str(self.numero)

def monta_arquivo_questao(questao, nome_arquivo):
    return "{}/{}/{}".format(questao.turma, questao.numero, nome_arquivo)

class ArquivosQuestao(models.Model):
    questao = models.ForeignKey(Questao)
    arquivo = models.FileField(upload_to=monta_arquivo_questao)

    class Meta:
        unique_together = (('questao', 'arquivo'),)

    def __str__(self):
        return self.questao