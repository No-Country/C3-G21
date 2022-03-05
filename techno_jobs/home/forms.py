from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# from .models import Company, Offer

# from .constants import COUNTRY_CHOICES

# class UserRegisterForm(UserCreationForm):
#     # FIXME: buscar como agregar un checkbox para definir el user, si es perfil o compañia

#     email = forms.EmailField(required=True)
#     # help_text es lo que aparece en el input
#     # widget será cómo aparecerá en el HTML (con *****)
#     # las variables tienen que ser password1 y password2 porque así lo determina django para la pass y la confirmacion
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=20, required=True)
#     password2 = forms.CharField(label='Confirma tu contraseña', widget=forms.PasswordInput, max_length=20, required=True)
# # TODO: UserProfileForm con el perfil completo del user
#     name = forms.CharField(max_length=30)
#     lastname = forms.CharField(max_length=30)
#     cv = forms.FileField(required=True)

#     class Meta:
#         """
#         Va a ser donde vamos a asociar la form en model
#         """
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'name', 'lastname', 'cv']
#         help_texts = { p: '' for p in fields }

# class CompanyRegisterForm(UserCreationForm):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField(required=True)
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

from django.forms import ModelForm
from .models import User, Company, Offer

class UsuarioForm(ModelForm):
    cv = forms.FileField(required=True)

    class Meta:
        model = User
        fields = ['name', 'lastname', 'email', 'password1', 'password2', 'cv']
        help_texts = { p: '' for p in fields }


class CompaniaForm(ModelForm):

    class Meta:
        model = Company
        fields = ['company_name', 'email', 'password1', 'password2', 'location', 'phone', 'web']
        help_texts = { p: '' for p in fields }

class OfferForm(ModelForm):

    class Meta:
        model = Offer
        fields = '__all__'
        help_texts = { p: '' for p in fields }