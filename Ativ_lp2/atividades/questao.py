from datetime import datetime 

class Questao():
    def __init__(self):
        self.data_limite_entrega = datetime.now()

    def obter_alunos_sem_tarefa(self):
        return ['Lucas', 'Matheus', 'Guilherme']

