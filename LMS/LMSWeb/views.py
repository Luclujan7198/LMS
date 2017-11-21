from django.shortcuts import render
from core.models import Curso

def index(request):
    return render(request, 'LMSWeb/index.html')

def cursos(request):
    contexto = {
        "cursos": Curso.objects.all()
    }
    return render(request, 'LMSWeb/cursos.html', contexto)

def curso(request, curso_id):
    return render(request, 'LMSWeb/curso.html', { 'curso_id': curso_id })

def noticias(request):
    return render(request, 'LMSWeb/noticias.html')

def noticia(request, noticia_id):
    return render(request, 'LMSWeb/noticia.html', { 'noticia_id': noticia_id })

def contato(request):
    return render(request, 'LMSWeb/contato.html')

def cancelamento_matricula(request):
    return render(request, 'LMSWeb/cancelamento_matricula.html')

def matriculaonline(request):
    return render(request, 'LMSWeb/matriculaonline.html')
