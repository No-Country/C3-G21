from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User, UserProfile, CompanyProfile

class EditUserForm(forms.ModelForm):
    # first_name y last_name viene de User, lo demás de UserProfile
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            }), required=False
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            }), required=False
    )
    class Meta:
        model = User
        fields = ('first_name','last_name')

class EditUserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label='Foto de perfil',required=False, widget=forms.FileInput)
    cv = forms.FileField(label='Subir CV',required=False, widget=forms.FileInput)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    url = forms.URLField(label='Website URL', widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=60, required=False)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=260, required=False)

    class Meta:
        model = UserProfile
        fields = ('avatar', 'cv', 'location', 'url', 'bio')

class EditCompanyProfileForm(forms.ModelForm):
    logo = forms.ImageField(label='Logo',required=False, widget=forms.FileInput)
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=260, required=False)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=15, required=False)
    web = forms.URLField(label='Website URL', widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=60, required=False)

    class Meta:
        model = CompanyProfile
        fields = ('logo', 'company_name','bio', 'location', 'phone', 'web')

# class OfferCreation(UserCreationForm):
#     pass
class OfferForm(ModelForm):
    pass
    # class Meta:
    #     model = Offer
    #     fields = '__all__'
    #     help_texts = { p: '' for p in fields }