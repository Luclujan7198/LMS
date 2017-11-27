class Disciplina():
    def __init__(self,nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def Media_Boletim(self,nota1,nota2):
        return (nota1 + nota2) /2


class Matematica(Disciplina):
    contador_de_testes = 0
    matriculados = 40

    def __init__(self,nota1,nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def Media_Boletim(self):
        return(self.nota1 + self.nota2) /2
    
    def verificador_matricula(self):
        media_alunos = [6.25,5.0]
        media = Media_Boletim()
        if media > max(media_alunos):
            return True
        else:
            return False

    def matricular(self):
        if verificador_matricula() == True:
            self.matriculados = self.matriculados + 1
            return print('matriculado com sucesso!')
        elif self.matriculados < 40:
            self.matriculados = self.matriculados + 1
            return print('matriculado com sucesso!')
        else:
            return print('Impossivel matricula nessa materia! \nTurmas ja preenchida!')
            
                

    def aumentar_contador_de_testes(self):
        self.contador_de_testes + 1

a = Matematica(5.0,7.5)
print(a.Media_Boletim())
print(a.matricular())


