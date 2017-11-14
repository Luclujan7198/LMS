from disciplina import *


class Aluno(Disciplina):
    materia = 'ingles'

    def __init__(self, nome, ra):
        self.contador_de_testes = Matematica.contador_de_testes
        self.nome = nome
        self.ra = ra


    def enviar_tarefa(self):
        return True

    def verificador_de_teste(self):
        if Matematica.contador_de_testes == 0:
            print('Prova disponivel')
        else:
            print('Você ja fez o teste!!!')

    def matricula(self, materia):
        if self.materia != materia:
            self.materia = materia
            print(self.materia,'Aluno cadastrado com sucesso!!')
        elif  materia == self.materia:
            print('Impossivel se cadastrar na mesma materia!!!')
        
    
aluno = Aluno('lucas',1233215)
print(aluno.verificador_de_teste())
print(aluno.matricula('ingles'))
    

