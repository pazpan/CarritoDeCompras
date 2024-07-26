from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm): # Definición del formulario RegistrationForm que hereda de UserCreationForm
    class Meta: # Clase Meta para especificar el modelo y los campos que se usarán en el formulario
        model = User # El formulario se basa en el modelo User
        fields = ('username','email', 'password1', 'password2')  