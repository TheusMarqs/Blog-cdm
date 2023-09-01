from django.shortcuts import render
from braces.views import GroupRequiredMixin
from django.views.generic.list import ListView
from django.contrib.messages import constants
from django.views import View
from textos.models import Texto
from django.core.mail import send_mail

def home(request):
    textos = Texto.objects.order_by('-dataCriacao')
    return render(request, 'home.html', {'textos': textos})

def contato(request):
    return render(request, 'home.html')