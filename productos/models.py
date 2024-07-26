from django.db import models

# Create your models here.
from django.db import models

from categorias.models import Categoria



# Create your models here.
class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=20) 
    precio = models.IntegerField(default=0) 
    stock = models.IntegerField(default=0)  
    descripcion = models.CharField(max_length=20)  
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.nombre 