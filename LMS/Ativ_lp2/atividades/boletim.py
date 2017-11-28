class Boletim():
    def __init__(self, turma, aluno, nota1, nota2):
        self.turma = turma
        self.aluno = aluno
        self.nota1 = nota1
        self.nota2 = nota2

    def Media_Boletim(self):
        return (self.nota1 + self.nota2) / 2