from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import constants
from .models import Texto
from .forms import TextoForm

class TextoCreate(CreateView):
    model = Texto
    form_class = TextoForm
    template_name = 'cadastrar_texto.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        submitBtn = 'Cadastrar'
        context['submitBtn'] = submitBtn

        return context

class TextoUpdate(UpdateView):
    model = Texto
    fields = ['titulo', 'texto', 'dataCriacao', 'imagem']
    template_name = 'cadastrar_texto.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        submitBtn = 'Editar'
        context['submitBtn'] = submitBtn

        return context

class TextoDelete(DeleteView):
    model = Texto
    template_name = 'home.html'
    success_url = reverse_lazy('home')

def exibir_texto(request, id):
    textos = Texto.objects.filter(id=id)
    return render(request, 'exibir_texto.html', {'textos': textos})