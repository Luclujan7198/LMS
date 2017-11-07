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

class Noticia():
    def __init__(self):
        self.titulo = ''
        self.image = ''
        self.text = ''

    def GetNoticia(self, noticia_id):
        noticia = self
        noticia.titulo = 1
        noticia.image = 'noticia1.png'
        noticia.text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        return noticia