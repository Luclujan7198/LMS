from django.shortcuts import render

from .models import Curso
from .models import Disciplina
from .models import DisciplinaOfertada
# Create your views here.



# Create your views here.
def cadastro_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'cadastro_cursos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de cursos',
#            'cursos': ['' , '', ''],
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )

def cadastro_alunos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'cadastro_alunos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de Alunos',
#            'Alunos': ['' , '', ''],
            'Alunos': Alunos.objects.all(),
            'year':datetime.now().year,
        })
    )

