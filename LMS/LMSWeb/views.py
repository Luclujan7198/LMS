from django.shortcuts import render

def index(request):
    return render(request, 'LMSWeb/index.html')

def cursos(request):
    return render(request, 'LMSWeb/cursos.html')

def curso(request, curso_id):
    return render(request, 'LMSWeb/curso.html', { 'curso_id': curso_id })

def noticias(request):
    return render(request, 'LMSWeb/noticias.html')

def noticia(request, noticia_id):
    return render(request, 'LMSWeb/noticia.html', { 'noticia_id': noticia_id })

def contato(request):
    return render(request, 'LMSWeb/contato.html')
def teste(request):
    return render(request, 'LMSWeb/testes.html')

def cancelamento_matricula(request):
    return render(request, 'LMSWeb/cancelamento_matricula.html')


