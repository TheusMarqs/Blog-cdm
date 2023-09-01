from django import forms
from .models import Texto

class TextoForm(forms.ModelForm):
    class Meta:
        model = Texto
        fields = ['titulo', 'texto', 'dataCriacao', 'imagem']
        widgets = {
            'dataCriacao': forms.DateInput(attrs={'type': 'date'}),
            'texto': forms.Textarea(attrs={'rows': 7}),
        }