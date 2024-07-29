from django.urls import path
from . import views

urlpatterns = [
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
]
