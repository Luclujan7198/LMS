class Professor():
    def __init__(self,nome, ra):
        self.nome = nome
        self.ra = ra

    def confirmar_matricula(self, matricula):
        pode_matricular = matricula.verificar_matricula()

        return pode_matricular
        # if pode_matricular:
        #     print('Matriculado')
        # else:
        #     print('Impossível matricular nessa matéria!')



