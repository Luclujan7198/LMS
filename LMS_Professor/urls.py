from django.conf.urls import url
from . import views

app_name = 'LMS_Professor'


urlpatterns = [
    url(r'^testes/$', views.teste, name='teste'),
    url(r'^$', views.index, name='index'),
]