from django.shortcuts import render

def index(request):
    return render(request, 'LMSWeb/index.html')

def cursos(request):
    return render(request, 'LMSWeb/testes.html')