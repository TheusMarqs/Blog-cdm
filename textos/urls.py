from django.urls import path
from .views import TextoCreate, TextoUpdate, TextoDelete
from . import views

urlpatterns = [
    path('cadastrar_texto', TextoCreate.as_view(), name='cadastrar_texto'),
    path('exibir_texto<int:id>', views.exibir_texto, name='exibir_texto'),
    path('update_texto/<int:pk>', TextoUpdate.as_view(), name='update_texto'),
    path('delete_texto/<int:pk>', TextoDelete.as_view(), name='delete_texto'),
]