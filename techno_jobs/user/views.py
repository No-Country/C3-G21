from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        # accedemos a la información que se envió en el form
        form = UserRegisterForm(request.POST)
        # verificamos validez de la form (si se llenó correctamente)
        if form.is_valid():
            #si la form es válida, accedemos a los datos
            form.save()
            username = form.cleaned_data['username']
            print(username)

            # autenticar
            user = authenticate(username=username, password=form.cleaned_data['password1'])
            login(request, user)

            #FIXME: mensaje de éxito [toastr]
            messages.success(request, f'Usuario {username} ha sido creado')
            return redirect(to='user:user-profile')
    else: 
        form = UserRegisterForm()
    context = { 'form': form }
    return render(request, 'user/register.html', context)

def user_profile(request):
    return render(request, 'user/user-profile.html')

def logout_view(request):
    logout(request)
    # FIXME: toastr
    messages.success(request, f'Has cerrado sesión correctamente')
    return redirect(to='home:index')
