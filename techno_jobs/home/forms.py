from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Company, Offer

from .constants import COUNTRY_CHOICES

class UserRegisterForm(UserCreationForm):
    # FIXME: buscar como agregar un checkbox para definir el user, si es perfil o compañia

    email = forms.EmailField(required=True)
    # help_text es lo que aparece en el input
    # widget será cómo aparecerá en el HTML (con *****)
    # las variables tienen que ser password1 y password2 porque así lo determina django para la pass y la confirmacion
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=20, required=True)
    password2 = forms.CharField(label='Confirma tu contraseña', widget=forms.PasswordInput, max_length=20, required=True)
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)

    class Meta:
        """
        Va a ser donde vamos a asociar la form en model
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'lastname']
        help_texts = { p: '' for p in fields }

# TODO: UserProfileForm con el perfil completo del user
class UserProfileForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)
    # profile_pic = forms
    cv = forms.FileField(required=True)

class CompanyRegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=20, required=True)
    password2 = forms.CharField(label='Confirma tu contraseña', widget=forms.PasswordInput, max_length=20, required=True)
    company_name = forms.CharField(max_length=150, required=True)
    location = forms.ChoiceField(choices=COUNTRY_CHOICES)
    phone = forms.IntegerField()
    web = forms.CharField(max_length=200, required=False)

    class Meta:
        """
        Va a ser donde vamos a asociar la form en model
        """
        model = Company
        fields = ['username', 'email', 'password1', 'password2', 'company_name', 'location', 'phone', 'web']
        help_texts = { p: '' for p in fields }