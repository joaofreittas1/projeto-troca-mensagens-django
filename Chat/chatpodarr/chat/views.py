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

def room(request, room):
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Sala.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Sala.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)