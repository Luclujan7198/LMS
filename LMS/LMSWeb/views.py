from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def cancelamento_matricula(request):
    return render(request, 'LMSWeb/cancelamento_matricula.html')

def matriculaonline(request):
    return render(request, 'LMSWeb/matriculaonline.html')

def login(request):
    if request.method == "POST":
        ra = request.POST['ra']
        password = request.POST['password']
        user = authenticate(request, ra=ra, password=password)
        if user is not None:
            auth_login(request, user)

            if user.groups.filter(name='Professores').exists():
                return HttpResponseRedirect(reverse('LMS_Professor:index'))
            else:
                return HttpResponseRedirect(reverse('admin:index'))
        else:
            errorMessage = 'Login Inválido'
            return render(request, 'LMSWeb/login.html', {'errorMessage': errorMessage})
    else:
        return render(request, 'LMSWeb/login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'LMSWeb/index.html')
