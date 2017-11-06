from django.conf.urls import url
from . import views

app_name = 'LMSWeb'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^testes/', views.cursos, name='testes')
]