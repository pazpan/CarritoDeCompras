from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm, UserProfileForm
from .models import UserProfile



def registrar_usuario(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('listar_usuarios')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'registrar_usuario.html', context)

def listar_usuarios(request):
    usuarios = UserProfile.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})
