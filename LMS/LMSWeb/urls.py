from django.conf.urls import url
from . import views

app_name = 'LMSWeb'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cursos/$', views.cursos, name='cursos'),
    url(r'^cursos/(?P<curso_id>[0-9]+)/$', views.curso, name='curso')
]