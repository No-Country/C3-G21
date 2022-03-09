from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import *
from .forms import EditUserForm, EditUserProfileForm, EditCompanyProfileForm, CreateCompanyForm

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

class DeleteUser(DeleteView):
    model = User
    template_name = 'home/delete-user.html'
    success_url = reverse_lazy('home:index')

# ----- Company -----
# class CreateCompanyProfile(CreateView):
#     model = CompanyProfile
#     form_class = CreateCompanyForm
#     template_name = 'home/company-signup.html'
#     success_url = reverse_lazy('home:index')

def create_company(request):
    if request.method == 'POST':
        form_company = CreateCompanyForm(request.POST, request.FILES)
        if form_company.is_valid():
            form_company.save()

            username = form_company.cleaned_data['username']
            username = form_company.cleaned_data['email']
            user = authenticate(username=username, password=form_company.cleaned_data['password1'])
            login(request, user)
            return redirect(to='home:company-profile')
    else: 
        form_company = CreateCompanyForm()
    context = { 'form_company': form_company }
    print(context)
    return render(request, 'home/company-signup.html', context)

class CompanyProfileView(DetailView):
    model = CompanyProfile

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(CompanyProfile, pk=pk)

        context = {
            'user': user,
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

class DeleteCompany(DeleteView):
    model = CompanyProfile
    template_name = 'home/delete-company.html'
    success_url = reverse_lazy('home:index')

def logout_view(request):
    logout(request)
    # FIXME: toastr
    messages.success(request, f'Has cerrado sesión correctamente')
    return redirect(to='home:index')
