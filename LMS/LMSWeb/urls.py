from django.conf.urls import url
from . import views

app_name = 'LMSWeb'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^cursos/$', views.cursos, name='cursos'),
    url(r'^cursos/(?P<curso_id>[0-9]+)/$', views.curso, name='curso'),
    url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^noticias/(?P<noticia_id>[0-9]+)/$', views.noticia, name='noticia'),
    url(r'^contato/$', views.contato, name="contato"),
]