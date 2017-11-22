from django.shortcuts import render

# Create your views here.

def teste(request):
    return render(request, 'LMS_Professor/testes.html')

def index(request):
    return render(request, 'LMS_Professor/index.html')
