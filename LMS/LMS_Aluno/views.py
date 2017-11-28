from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def usuario_is_aluno(user):
    return user.groups.filter(name='Alunos').exists()


@user_passes_test(usuario_is_aluno, login_url='/login')
def index(request):
    return render(request, 'LMS_Aluno/index.html')

@user_passes_test(usuario_is_aluno, login_url='/login')
def boletim(request):
    return render(request, 'LMS_Aluno/boletim.html')