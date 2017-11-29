from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def usuario_is_professor(user):
    return user.groups.filter(name='Professores').exists()


@user_passes_test(usuario_is_professor, login_url='/login')
def teste(request):
    return render(request, 'LMS_Professor/testes.html')

@user_passes_test(usuario_is_professor)
def index(request):
    return render(request, 'LMS_Professor/index.html')
