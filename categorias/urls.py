from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar_categoria),
    path('Guardar_categoria/', views.Guardar_categoria),
    path('Editar_categoria/<id_categoria>', views.Editar_categoria,name='Editar_categoria'),
    path('Eliminar_categoria/<id_categoria>', views.Eliminar_categoria,name='Eliminar_categoria'),
]
