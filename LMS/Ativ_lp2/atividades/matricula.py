class Matricula():
    def __init__(self, aluno, turma):
        self.aluno = aluno
        self.turma = turma
    
    def obter_num_alunos_matriculados(self):
        return 22

    def verificar_num_alunos(self):
        max_alunos = self.turma.max_alunos
        alunos_matriculados = self.obter_num_alunos_matriculados()

        if alunos_matriculados >= max_alunos:
            return False
        else:
            return True
        
    def verificar_media_aluno(self):
        media_sala = 7 # get media disciplina

        if self.aluno.get_media_aluno() > media_sala:
            return True
        else:
            return False

    def verificar_ordem_matricula(self):
        return True

    def verificar_aluno_ja_cadastrado(self):
        aluno_ja_cadastrado = False # busca no banco
        return aluno_ja_cadastrado

    def verificar_matricula(self):
        if self.verificar_media_aluno() and self.verificar_ordem_matricula() and self.verificar_num_alunos():
            return True
        else:
            return False

    def matricular(self):
        if self.verificar_aluno_ja_cadastrado():
            print ('Aluno já matriculado nesta turma')
            return

        verifica_num_alunos = self.verificar_num_alunos()
        if verifica_num_alunos:
            return 'Matriculado'
        else:
            return 'Matriculado (Turma cheia)'
        

