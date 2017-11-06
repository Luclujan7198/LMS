from django.shortcuts import render

from .models import Curso

def index(request):
    return render(request, 'LMSWeb/index.html')

def cursos(request):
    return render(request, 'LMSWeb/cursos.html')

def curso(request, curso_id):
    model = Curso()
    curso = model.GetCurso(curso_id)
    return render(request, 'LMSWeb/curso.html', { 'curso': curso })