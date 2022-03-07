from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import UserProfile

from .constants import COUNTRY_CHOICES


class EditUserProfileForm(forms.ModelForm):
    # first_name y last_name viene de User, lo demás de UserProfile
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
    avatar = forms.ImageField(label='Profile Picture',required=False, widget=forms.FileInput)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    url = forms.URLField(label='Website URL', widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=60, required=False)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=260, required=False)

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','avatar','location','url','bio')



class CompanyRegisterForm(UserCreationForm):
    pass
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=20, required=True)
#     password2 = forms.CharField(label='Confirma tu contraseña', widget=forms.PasswordInput, max_length=20, required=True)
#     company_name = forms.CharField(max_length=150, required=True)
#     location = forms.ChoiceField(choices=COUNTRY_CHOICES)
#     phone = forms.IntegerField()
#     web = forms.CharField(max_length=200, required=False)

#     class Meta:
#         """
#         Va a ser donde vamos a asociar la form en model
#         """
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'company_name', 'location', 'phone', 'web']
#         help_texts = { p: '' for p in fields }

# class OfferCreation(UserCreationForm):
#     pass
class OfferForm(ModelForm):
    pass
    # class Meta:
    #     model = Offer
    #     fields = '__all__'
    #     help_texts = { p: '' for p in fields }