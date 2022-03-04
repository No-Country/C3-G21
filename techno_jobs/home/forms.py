from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    # FIXME: buscar como agregar un checkbox para definir el user, si es perfil o compañia

    email = forms.EmailField(required=True)
    # help_text es lo que aparece en el input
    # widget será cómo aparecerá en el HTML (con *****)
    # las variables tienen que ser password1 y password2 porque así lo determina django para la pass y la confirmacion
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=20)
    password2 = forms.CharField(label='Confirma tu contraseña', widget=forms.PasswordInput, max_length=20)

    class Meta:
        """
        Va a ser donde vamos a asociar la form en model
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { p: '' for p in fields }

# TODO: UserProfileForm con el perfil completo del user