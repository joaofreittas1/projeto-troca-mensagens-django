import django
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name= 'login') ,
    path('telaprincipal/', views.telaprincipal, name= 'telaprincipal'),
    path('', views.chat, name= 'chat'),
    path('<str:room>/', views.sala, name='sala'),
    path('carregaview', views.carregaview, name='carregaview'),
    path('send', views.enviar, name='enviar'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),  
 ] 