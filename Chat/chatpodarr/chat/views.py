from optparse import Values
from django.http import HttpResponse, JsonResponse
from email import message
from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.shortcuts import render,redirect
from chat.models import Sala,Mensagem

# Create your views here.

def login(request):
    return render(request, 'login.html')

def telaprincipal(request):
    return render(request, 'telaprincipal.html')

def chat(request):
    return render(request, 'chat.html')

def sala(request, room):
    username = request.GET.get('username')
    details_room = Sala.objects.get(name=room)
    return render(request, 'sala.html', {'username': username, 'room' : room, 'details_room' : details_room})

def carregaview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Sala.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        return redirect ('/login')#Ainda em fase de implantação, para que caso não exista serviços iguais ao que a podarr tenha, seja alertado o usuario

def enviar(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Mensagem.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Messagem enviada com sucesso')

def getMessages(request, room):
    details_room = Sala.objects.get(name=room)
    messages = Mensagem.objects.filter(room= details_room.id) 
    return JsonResponse ({"Mensagem:":list(messages.values())})
  
   