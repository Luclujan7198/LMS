from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'LMS_Aluno/index.html')

def boletim(request):
    return render(request, 'LMS_Aluno/boletim.html')