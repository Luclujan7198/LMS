from django.contrib import admin
from .models import Curso
from .models import Disciplina

admin.site.register(Curso)
admin.site.register(Disciplina)