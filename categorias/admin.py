from django.contrib import admin
from categorias.models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display =('id_categoria','nombre')
    
admin.site.register(Categoria, CategoriaAdmin)