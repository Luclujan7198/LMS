from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
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

def login(request):
    error = None

    if request.method == "POST":
        ra = request.POST['ra']
        password = request.POST['password']
        user = authenticate(request, ra=ra, password=password)
        if user is not None:
            auth_login(request, user)

            if user.groups.filter(name='Professores').exists():
                return redirect(reverse('LMS_Professor:index'))
            elif user.groups.filter(name='Coordenadores').exists():
                return redirect(reverse('admin:index'))
            elif user.groups.filter(name='Alunos').exists():
                return redirect(reverse('LMS_Aluno:index'))
            else:
                error = "Usuário não pertence a nenhum grupo"
        else:
            error = "Usuário ou senha inválidos"
    else:
        if request.user.is_authenticated:
            return redirect(reverse('LMSWeb:index'))

    return render(request, 'LMSWeb/login.html', {'error': error})

def logout(request):
    auth_logout(request)
    return render(request, 'LMSWeb/index.html')
