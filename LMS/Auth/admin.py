from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Usuario, Aluno, Professor

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['ra', 'nome', 'email', 'curso']
    
    def save_m2m(self):
        group = Group.objects.get(name='Alunos')
        self.instance.groups.add(group)

    def save(self, commit=True):
        instance = super(NovoAlunoForm, self).save()
        instance.set_password('@lms2017')
        self.save_m2m()
        return instance

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'curso']

class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm

    list_display = ('nome', 'email', 'curso')
    list_filter = ('curso',)
    fieldsets = ( (None, {'fields': ('nome', 'email', 'curso')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'email', 'curso')} ),)
    search_fields = ('nome',)
    ordering = ('nome',)
    filter_horizontal = ()

admin.site.register(Aluno, AlunoAdmin)


class NovoProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['ra', 'nome', 'email', 'telefone']
    
    def save_m2m(self):
        group = Group.objects.get(name='Professores')
        self.instance.groups.add(group)

    def save(self, commit=True):
        instance = super(NovoProfessorForm, self).save()
        instance.set_password('@lms2017')
        self.save_m2m()
        return instance

class AlterarProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'telefone']

class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm

    list_display = ('nome', 'email', 'telefone')
    list_filter = ()
    fieldsets = ( (None, {'fields': ('nome', 'email', 'telefone')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'email', 'telefone')} ),)
    search_fields = ('nome',)
    ordering = ('nome',)
    filter_horizontal = ()

admin.site.register(Professor, ProfessorAdmin)