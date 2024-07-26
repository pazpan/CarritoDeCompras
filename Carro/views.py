from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login



def home(request):
    return render(request,'home.html')



def registrarse(request):
    if request.method == 'POST':      
        try: #controlar errores 
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                 #Muestra mensajes de exito
                messages.success(request, "Registrado con éxito")
                return redirect('registrarse') # Redirigir a la misma página para más registros
            else: #Muestra mensajes de error
                messages.error(request, "Datos ingresados invalidos o ya existen")
                return render(request, 'registrarse.html', {'form': form})
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {e}")
            return render(request, 'registrarse.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registrarse.html', {'form': form})
    
    
    
    
# Función para iniciar sesión de usuarios
def login(request):
    #controlar errores 
    try:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home') # Redirigir al usuario a la página de inicio después del inicio de sesión
            else: #Muestra los mensajes de error
                messages.error(request, 'Datos ingresados invalidos')
        else:
            form = AuthenticationForm()
        
        return render(request, 'login.html', {'form': form})
    
    except Exception as e:  # Capturar y manejar cualquier excepción que ocurra durante la actualización
        messages.error(request, f'ocurrió un error inesperado: {e}')
        return redirect('login')


# Función para cerrar sesión de usuarios
def logout(request):
    auth.logout(request)
    return redirect('home') # Redirige a la pagina de inicio