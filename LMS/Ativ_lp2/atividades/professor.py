from aluno import Aluno

class professor(Aluno):
    def __init__(self,nome, ra):
        self.nome = nome
        self.ra = ra

    def receber_tarefa(self):
        if not Aluno.tarefa:
            return print('tarefa não recebida')
        else:
            return print('tarefa recebida')

professor = professor('alguem',123321)
print(professor.receber_tarefa())