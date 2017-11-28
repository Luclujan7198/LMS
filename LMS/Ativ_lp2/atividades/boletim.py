class Boletim():
    def __init__(self, turma, aluno, nota1, nota2):
        self.turma = turma
        self.aluno = aluno
        self.nota1 = nota1
        self.nota2 = nota2

    def Media_Boletim(self):
        return (self.nota1 + self.nota2) / 2

turma = 'ADS2B-TecnologiaWeb' #Turma.objects.get(pk=1)
aluno = '1701419' #Aluno.objects.get(ra=1701419)
nota1 = 8.00
nota2 = 5.00

boletim = Boletim(turma, aluno, nota1, nota2)
print(str(boletim.Media_Boletim()))