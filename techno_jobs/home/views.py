from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from .models import *
from .forms import EditUserForm, EditUserProfileForm, EditCompanyProfileForm

# Create your views here.
User = get_user_model() # lo usamos en el UserProfileView

def home(request):
    return render(request, 'home/index.html')

def faq(request):
    return render(request, 'home/faq.html')

class EditUser(UpdateView):
    model = User
    form_class = EditUserForm
    template_name = "home/edit-user.html"
    success_message = "Usuario actualizado correctamente"

    def get_success_url(self):
        user = self.get_object()
        if user.profile.is_professional:
            return reverse_lazy('home:user-profile', kwargs={ 'pk': user.id })
        elif user.company_profile.is_company:
            return reverse_lazy('home:company-profile', kwargs={ 'pk': user.id })

# ----- User -----
class UserProfileView(DetailView):
    model = UserProfile

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        profile = UserProfile.objects.get(user=user)

        context = {
            'user': user,
            'profile': profile,
        }
        return render(request, 'home/userprofile_detail.html', context)

class EditUserProfile(UpdateView):
    model = UserProfile
    form_class = EditUserProfileForm
    template_name = "home/edit-profile.html"
    success_message = "Usuario actualizado correctamente"
    # success_url = None

    def get_success_url(self):
        profile = self.get_object()
        user = profile.user
        return reverse_lazy('home:user-profile', kwargs={ 'pk': user.id })

# ----- Company -----
class CompanyProfileView(DetailView):
    model = CompanyProfile

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        profile = CompanyProfile.objects.get(user=user)

        context = {
            'user': user,
            'company-profile': profile,
        }
        return render(request, 'home/companyprofile_detail.html', context)

class EditCompanyProfile(UpdateView):
    model = CompanyProfile
    form_class = EditCompanyProfileForm
    template_name = "home/edit-company-profile.html"
    success_message = "Usuario actualizado correctamente"
    # success_url = None

    def get_success_url(self):
        profile = self.get_object()
        user = profile.user
        return reverse_lazy('home:edit-company-profile', kwargs={ 'pk': user.id })


def logout_view(request):
    logout(request)
    # FIXME: toastr
    messages.success(request, f'Has cerrado sesión correctamente')
    return redirect(to='home:index')
