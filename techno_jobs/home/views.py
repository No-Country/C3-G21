from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def faq(request):
    return render(request, 'home/faq.html')

def register(request):
    if request.method == 'POST':
        # accedemos a la información que se envió en el form
        form = UserRegisterForm(request.POST)
        # verificamos validez de la form (si se llenó correctamente)
        if form.is_valid():
            # guardamos
            form.save()
            # si la form es válida, accedemos a los datos
            username = form.cleaned_data['username']
            print(username)

            # autenticar
            user = authenticate(username=username, password=form.cleaned_data['password1'])
            login(request, user)

            #FIXME: mensaje de éxito [toastr]
            messages.success(request, f'Usuario {username} ha sido creado')
            return redirect(to='home/user-profile.html')
    else: 
        form = UserRegisterForm()
    context = { 'form': form }
    return render(request, 'home/register.html', context)

def user_profile(request):
    return render(request, 'home/user-profile.html')

def logout_view(request):
    logout(request)
    # FIXME: toastr
    messages.success(request, f'Has cerrado sesión correctamente')
    return redirect(to='home/index.html')
