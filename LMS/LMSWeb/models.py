from django.db import models

class Curso():
    def __init__(self):
        self.id = 0
        self.nome = '',
        self.duracao = '',
        self.modalidade = '',
        self.periodo = ''

    def GetCurso(self, curso_id):
        curso = self
        curso.id = 1
        curso.nome = 'Administração'
        curso.duracao = '5 semestres'
        curso.modalidade = 'Presencial'
        curso.periodo = 'matutino, noturno'
        return curso
