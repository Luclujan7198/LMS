from django.conf.urls import url
from . import views

app_name = 'LMS_Aluno'


urlpatterns = [
    url(r'^$', views.index, name='index'),
]