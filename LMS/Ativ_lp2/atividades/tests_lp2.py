from aluno import Aluno
from boletim import Boletim
from questao import Questao
from resposta import Resposta
from matricula import Matricula
from turma import Turma
from professor import Professor
from datetime import datetime


def test_media_boletim():
    aluno = Aluno('Lucas', 1701419)
    turma = Turma('Tecnologia Web')

    boletim = Boletim(aluno, turma, 10, 8)
    assert boletim.Media_Boletim() == (10 + 8) / 2

def test_teste_online():
    aluno = Aluno('Lucas', 1701419)
    assert aluno.realizou_teste(datetime.now()) == True

def test_alunos_enviaram_tarefa():
    questao = Questao()
    assert questao.obter_alunos_sem_tarefa() == ['Lucas', 'Matheus', 'Guilherme']

def test_impedir_envio_tarefa_apos_prazo():
    questao = Questao()
    aluno = Aluno('Lucas', 1701419)
    resposta = Resposta(questao, aluno, datetime.now())

    assert resposta.pode_entregar() == True

def test_impedir_matricula_duplicada():
    aluno = Aluno('Lucas', 1701419)
    turma = Turma('Tecnologia Web') 

    matricula = Matricula(aluno, turma)
    assert matricula.verificar_aluno_ja_cadastrado() == False

def test_mensagem_max_alunos_matricula():
    aluno = Aluno('Lucas', 1701419)
    turma = Turma('Tecnologia Web') 

    matricula = Matricula(aluno, turma)
    assert matricula.matricular() == 'Matriculado (Turma cheia)'

def test_confirmacao_matricula():
    aluno = Aluno('Lucas', 1701419)
    turma = Turma('Tecnologia Web') 

    matricula = Matricula(aluno, turma)

    professor = Professor('Professor', 1)

    assert professor.confirmar_matricula(matricula) == False

    





    
