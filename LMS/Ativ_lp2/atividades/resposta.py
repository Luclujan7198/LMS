
class Resposta():
    def __init__(self, questao, aluno, data_envio):
        self.questao = questao
        self.aluno = aluno
        self.data_envio = data_envio

    def pode_entregar(self):
        if (self.data_envio > self.questao.data_limite_entrega):
            return False
        else:
            return True

    def salvar_resposta(self):
        if self.pode_entregar():
            print('Pode entregar')
        else:
            print('Tarefa fora do prazo!!!')