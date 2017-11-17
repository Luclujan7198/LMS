from django.contrib import admin
from .models import Curso
from .models import Disciplina
from .models import DisciplinaOfertada

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)