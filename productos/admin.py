from django.contrib import admin
from .models import Productos
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display =('id_producto','nombre','precio','stock','descripcion','categoria')

admin.site.register(Productos,ProductoAdmin)