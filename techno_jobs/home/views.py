from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from .models import *
from .forms import UsuarioForm, CompaniaForm

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def faq(request):
    return render(request, 'home/faq.html')

def register_user(request):
    if request.method == 'POST':
        # accedemos a la información que se envió en el form
        form = UsuarioForm(request.POST)
        # verificamos validez de la form (si se llenó correctamente)
        if form.is_valid():
            # guardamos
            form.save()
            if user.is_professional:
                group = Group.objects.get(name='professional')
                user.groups.add(group)
            # si la form es válida, accedemos a los datos
            username = form.cleaned_data['email']
            # autenticar
            user = authenticate(username=username, password=form.cleaned_data['password1'])
            login(request, user)

            #FIXME: mensaje de éxito [toastr]
            return redirect(to='home:user-profile')
    else: 
        form = UsuarioForm()
    context = { 'form': form }
    return render(request, 'home/register-user.html', context)

def register_company(request):
    if request.method == 'POST':
        form_company = CompaniaForm(request.POST)
        if form_company.is_valid():
            form_company.save()
            if user.is_company:
                group = Group.objects.get(name='company')
                user.groups.add(group)
            username = form_company.cleaned_data['email']
            user = authenticate(username=username, password=form_company.cleaned_data['password1'])
            login(request, user)
            return redirect(to='home:company-profile')
    else: 
        form_company = CompaniaForm()
    context = { 'form_company': form_company }
    return render(request, 'home/register-company.html', context)


def user_profile(request):
    return render(request, 'home:user-profile')

def company_profile(request):
    return render(request, 'home:company-profile')

def logout_view(request):
    logout(request)
    # FIXME: toastr
    messages.success(request, f'Has cerrado sesión correctamente')
    return redirect(to='home:index')
