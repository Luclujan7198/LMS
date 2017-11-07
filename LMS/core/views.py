from django.shortcuts import render
from .models import Curso

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