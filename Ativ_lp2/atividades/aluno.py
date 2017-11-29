
class Aluno():
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra

    def get_media_aluno(self):
        return 8

    def realizou_teste(self, data_teste):
        questoes_teste = ['1', '2', '3'] # Questao.objects.filter(data=data_teste)

        contador_resposta = 0
        for questao in questoes_teste:
            contador_resposta += 1 # Resposta.objects.filter(questao=questao).count() #Forma de puxar do banco 

        if contador_resposta == 0:
            return False
        else:
            return True

    def aplicar_teste(self):
        if self.realizou_teste:
            print('Você ja fez o teste!!!')
        else:
            print('Prova disponivel')
    

