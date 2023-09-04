from django.shortcuts import render, redirect
from braces.views import GroupRequiredMixin
from django.views.generic.list import ListView
from django.contrib.messages import constants
from django.views import View
from textos.models import Texto
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth import login

def home(request):
    textos = Texto.objects.order_by('-dataCriacao')
    grupo = request.user.groups.values_list('name', flat=True).first()

    return render(request, 'home.html', {'textos': textos, 'grupo': grupo})

def contato(request):
    return render(request, 'home.html')

class UsuarioCreate(CreateView):
    template_name = "cadastro.html"
    form_class = UsuarioForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Autentique o usuário após o registro
            login(request, user)
            
            # Redirecione para a página inicial ou outra página desejada
            return redirect('home')
        return render(request, self.template_name, {'form': form})