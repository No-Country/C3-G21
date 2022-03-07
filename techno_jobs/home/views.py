from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import EditUserProfileForm

# Create your views here.
User = get_user_model() # lo usamos en el UserProfileView

def home(request):
    return render(request, 'home/index.html')

def faq(request):
    return render(request, 'home/faq.html')

# def register_user(request):
#     if request.method == 'POST':
#         # accedemos a la información que se envió en el form
#         form = UserRegisterForm(request.POST, request.FILES)
#         # verificamos validez de la form (si se llenó correctamente)
#         if form.is_valid():
#             # guardamos
#             form.save()
#             # if user.is_professional:
#             #     group = Group.objects.get(name='professional')
#             #     user.groups.add(group)
#             # si la form es válida, accedemos a los datos
#             username = form.cleaned_data['username']
#             # autenticar
#             user = authenticate(username=username, password=form.cleaned_data['password1'])
#             login(request, user)

#             #FIXME: mensaje de éxito [toastr]
#             return redirect(to='home:user-profile')
    # else: 
    #     form = UserRegisterForm()
    # context = { 'form': form }
    # return render(request, 'home/register-user.html', context)

def register_company(request):
    pass
#     if request.method == 'POST':
#         form_company = CompanyRegisterForm(request.POST)
#         if form_company.is_valid():
#             form_company.save()
#             # if user.is_company:
#             #     group = Group.objects.get(name='company')
#             #     user.groups.add(group)
#             username = form_company.cleaned_data['username']
#             user = authenticate(username=username, password=form_company.cleaned_data['password1'])
#             login(request, user)
#             return redirect(to='home:company-profile')
#     else: 
#         form_company = CompanyRegisterForm()
#     context = { 'form_company': form_company }
#     return render(request, 'home/register-company.html', context)

# def user_profile(request):
#     # FIXME: pk tiene que obtener la primarykey del user
#     # context = { 'user': User.objects.get(pk=2) }
#     return render(request, 'home/user-profile.html')

class UserProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = UserProfile.objects.get(user=user)

        context = {
            'user': user,
            'profile': profile,
        }
        return render(request, 'home/user-profile.html', context)

@login_required
def EditUserProfile(request):
    user = request.user.id
    profile = UserProfile.objects.get(user__id=user)
    user_info = User.objects.get(id=user)

    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # lo que está en el User
            user_info.first_name = form.cleaned_data.get('first_name')
            user_info.last_name = form.cleaned_data.get('last_name')

            # lo que esta en el perfil
            profile.avatar = form.cleaned_data.get('avatar')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.bio = form.cleaned_data.get('bio')

            user_info.save()
            profile.save()

            return redirect('home:user-profile', username=request.user.username)
    else:
        form = EditUserProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home/edit-profile.html', context)





def company_profile(request):
    return render(request, 'home:company-profile')

def logout_view(request):
    logout(request)
    # FIXME: toastr
    messages.success(request, f'Has cerrado sesión correctamente')
    return redirect(to='home:index')
