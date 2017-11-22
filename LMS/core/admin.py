from django.contrib import admin
from .models import *


admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)
admin.site.register(Turma)
admin.site.register(Alunos)
admin.site.register(GradeCurricular)

