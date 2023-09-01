from django.db import models
import os

class Texto(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=15)
    texto = models.TextField()
    dataCriacao = models.DateField(verbose_name='Data de publicação')
    imagem = models.ImageField(verbose_name='Imagem', upload_to="img", blank=True, null=True)

    def delete(self, *args, **kwargs):
        # Antes de excluir o objeto, exclua também a imagem associada
        self.imagem.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.titulo