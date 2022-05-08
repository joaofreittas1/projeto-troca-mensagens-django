import django


from django.urls import path
from . import views

urlpatterns = [
    #path('', views.login, name= 'login') ,
    path('', views.chat, name= 'chat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    #path('telaprincipal/', views.telaprincipal, name= 'telaprincipal')
 ]