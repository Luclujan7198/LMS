class Aluno():
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra

    def realizou_teste(self, data_teste):
        questoes_teste = ['1', '2', '3'] # Questao.objects.filter(data=data_teste)

        contador_resposta = 0
        for questao in questoes_teste:
            contador_resposta += Resposta.objects.filter(questao=questao).count()

        if contador_resposta == 0:
            return False
        else:
            return True

    def enviar_tarefa(self):
        if not self.tarefa:
            return print('Tarefa não enviada')
        else:
            return print('Tarefa enviada')

    # def verificador_de_teste(self):
    #     if Matematica.contador_de_testes == 0:
    #         print('Prova disponivel')
    #     else:
    #         print('Você ja fez o teste!!!')

    def matricula(self, materia):
        if self.materia != materia:
            self.materia = materia
            print(self.materia,'Aluno cadastrado com sucesso!!')
        elif  materia == self.materia:
            print('Impossivel se cadastrar na mesma materia!!!')
        
    
aluno = Aluno('lucas',1233215)
print(aluno.realizou_teste())
print(aluno.matricula('ingles'))
print(aluno.enviar_tarefa())


