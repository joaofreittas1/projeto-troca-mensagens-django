from unicodedata import name
from django.db import models
from datetime import date, datetime


#OBSERVAÇAO, nas MODELS não rodar o comando para criar as tabelas (python manage.py makemigrations, python manage.py migrate)
#Ainda em fase de desenvolvimento da logica

# Create your models here.
class Sala(models.Model):
    name= models.CharField(max_length=250)

class Mensagem(models.Model):
    value = models.TextField() 
    date = models.DateTimeField(default = datetime.now, blank=True)
    user = models.CharField(max_length= 10000000)
    room = models.CharField(max_length= 10000000)

 