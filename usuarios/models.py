from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'Cliente'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    perfil = models.IntegerField(choices=USER_TYPE_CHOICES, default=2)

    def __str__(self):
        return f'{self.nombre} {self.apellidos} - {self.get_perfil_display()}'
