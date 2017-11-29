from django.db import models
from Auth.models import Usuario

class Curso(models.Model):
    sigla = models.CharField(max_length=10)
    nome = models.CharField(max_length=200)

    class Meta:
        unique_together = (('sigla', 'nome'),)

    def __str__(self):
        return self.nome

class Aluno(Usuario):
    usuario_id = models.OneToOneField(
        Usuario,
        primary_key=True,
        db_column='usuario_id',
        parent_link=True
    )

    curso = models.ForeignKey(Curso, default=True)

class Professor(Usuario):
    class Meta:
        verbose_name_plural = 'professores'
        
    usuario_id = models.OneToOneField(
        Usuario,
        primary_key=True,
        db_column='usuario_id',
        parent_link=True
    )

    telefone = models.CharField(max_length=11, blank=True, null=True)

class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=240, unique=True, default='')
    carga_horaria = models.IntegerField()
    teoria = models.DecimalField(decimal_places=2, max_digits=9)
    pratica = models.DecimalField(decimal_places=2, max_digits=9) 
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
        verbose_name_plural = 'disciplinas ofertadas'
    
    def __str__(self):
        return self.disciplina.nome + ' (' + str(self.ano) + '/' + self.semestre + ')'

class Turma(models.Model):
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada)
    id_turma = models.CharField(max_length=1)
    turno = models.CharField(max_length=15)
    professor = models.ForeignKey(Professor)

    class Meta:
        unique_together = (('disciplina_ofertada', 'id'),)

    def __str__(self):
        return 'Disciplina: ' + self.disciplina_ofertada.disciplina.nome + '(' + str(self.disciplina_ofertada.ano) + '/' + self.disciplina_ofertada.semestre + ')' + ' Turma: ' + self.id_turma

class GradeCurricular(models.Model):
    curso = models.ForeignKey(Curso)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=1)

    class Meta():
        unique_together = (('curso', 'ano', 'semestre'),)
        verbose_name = 'Grade Curricular'
        verbose_name_plural = 'Grades Curriculares'

    def __str__(self):
        return 'Curso: ' + self.curso.nome + '(' + str(self.ano) + '/' + self.semestre + ')'

class Periodo(models.Model):
    grade_curricular = models.ForeignKey(GradeCurricular)
    numero = models.IntegerField()

    class Meta:
        unique_together = (("grade_curricular", "numero"),)

    def __str__(self):
        return 'Curso: ' + self.grade_curricular.curso.nome + '(' + str(self.grade_curricular.ano) + '/' + self.grade_curricular.semestre + ')' + ' Numero: ' + str(self.numero)

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno)
    turma = models.ForeignKey(Turma)

    class Meta:
        unique_together = (('aluno', 'turma'),)

    def __str__(self):
        return self.aluno.nome + ' Disciplina: ' + self.turma.disciplina_ofertada.disciplina.nome + '(' + str(self.turma.disciplina_ofertada.ano) + '/' + self.turma.disciplina_ofertada.semestre + ')' + ' Turma: ' + self.turma.id_turma

class Questao(models.Model):
    turma = models.ForeignKey(Turma)
    numero = models.IntegerField()
    data_limite_entrega = models.DateField()
    descricao = models.TextField()
    data = models.DateField(auto_now=True)

    class Meta:
        unique_together = (('turma', 'numero'),)
        verbose_name_plural = 'Questoes'

    def __str__(self):
        return 'Disciplina: ' + self.turma.disciplina_ofertada.disciplina.nome + '(' + str(self.turma.disciplina_ofertada.ano) + '/' + self.turma.disciplina_ofertada.semestre + ')' + ' Turma: ' + self.turma.id_turma + ' Questao: ' + str(self.numero)

def monta_arquivo_questao(questao, nome_arquivo):
    return "{}/{}/{}".format(questao.turma, questao.numero, nome_arquivo)

class ArquivosQuestao(models.Model):
    questao = models.ForeignKey(Questao)
    arquivo = models.FileField(upload_to=monta_arquivo_questao)

    class Meta:
        unique_together = (('questao', 'arquivo'),)

    def __str__(self):
        return 'Disciplina: ' + self.questao.turma.disciplina_ofertada.disciplina.nome + '(' + str(self.questao.turma.disciplina_ofertada.ano) + '/' + self.questao.turma.disciplina_ofertada.semestre + ')' + ' Turma: ' + self.questao.turma.id_turma + ' Questao: ' + str(self.questao.numero) + ' Arquivo: ' + self.arquivo

class CursoTurma(models.Model):
    curso = models.ForeignKey(Curso)
    turma = models.ForeignKey(Turma)

    class Meta:
        unique_together = (('curso', 'turma'),)

    def __str__(self):
        return self.curso.nome + ' - Disciplina: ' + self.turma.disciplina_ofertada.disciplina.nome + '(' + str(self.turma.disciplina_ofertada.ano) + '/' + self.turma.disciplina_ofertada.semestre + ')' + ' Turma: ' + self.turma.id_turma 

class PeriodoDisciplina(models.Model):
    periodo = models.ForeignKey(Periodo)
    disciplina = models.ForeignKey(Disciplina)

    class Meta:
        unique_together = (('periodo','disciplina'),)

    def __str__(self): 
        return 'Curso: ' + self.periodo.grade_curricular.curso.nome + '(' + str(self.periodo.grade_curricular.ano) + '/' + self.periodo.grade_curricular.semestre + ')' + ' Numero: ' + str(self.periodo.numero) + ' Disciplina: ' + self.disciplina.nome

class Resposta(models.Model):
    questao = models.ForeignKey(Questao)
    aluno = models.ForeignKey(Aluno)
    data_avaliacao = models.DateField()
    nota = models.DecimalField(decimal_places=2,max_digits=4)
    avaliacao = models.TextField()
    descricao = models.TextField()
    data_de_envio = models.DateField(auto_now=True)

    class Meta:
        unique_together = (('questao','aluno'),)

    def __str__(self):
        return 'Disciplina: ' + self.questao.turma.disciplina_ofertada.disciplina.nome + '(' + str(self.questao.turma.disciplina_ofertada.ano) + '/' + self.questao.turma.disciplina_ofertada.semestre + ')' + ' Turma: ' + self.questao.turma.id_turma + ' Questao: ' + str(self.questao.numero) + ' Aluno: ' + self.aluno.nome

def monta_arquivo_resposta(resposta, nome_arquivo):
    return "{}/{}/{}".format(resposta.questao, resposta.aluno, nome_arquivo)

class ArquivosResposta(models.Model):
    resposta = models.ForeignKey(Resposta)
    arquivo = models.FileField(upload_to=monta_arquivo_resposta)

    class Meta:
        unique_together = (('resposta','arquivo'),)
    
    def __str__(self):
        return 'Disciplina: ' + self.resposta.questao.turma.disciplina_ofertada.disciplina.nome + '(' + str(self.resposta.questao.turma.disciplina_ofertada.ano) + '/' + self.questao.turma.disciplina_ofertada.semestre + ')' + ' Turma: ' + self.resposta.questao.turma.id_turma + ' Questao: ' + str(self.resposta.questao.numero) + ' Aluno: ' + self.resposta.aluno.nome + ' Arquivo: ' + self.arquivo

class Boletim(models.Model):
    turma = models.ForeignKey(Turma)
    aluno = models.ForeignKey(Aluno)
    nota1 = models.DecimalField(max_digits=4, decimal_places=2)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        unique_together = (('turma','aluno'),)
        verbose_name_plural = 'boletins'

    def __str__(self):
        return self.aluno.nome + ' - Disciplina: ' + self.turma.disciplina_ofertada.disciplina.nome + '(' + str(self.turma.disciplina_ofertada.ano) + '/' + self.turma.disciplina_ofertada.semestre + ')' + ' Turma: ' + self.turma.id_turma 