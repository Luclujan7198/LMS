from django.contrib import admin
from .models import *


admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)
admin.site.register(Turma)
admin.site.register(GradeCurricular)
admin.site.register(Periodo)
admin.site.register(Matricula)
admin.site.register(PeriodoDisciplina)
admin.site.register(Questao)
admin.site.register(ArquivosQuestao)
admin.site.register(Resposta)
admin.site.register(ArquivosResposta)
admin.site.register(CursoTurma)