from django.db import models
# from django.forms import ModelForm
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save # una señal, lo que ocurrira cuando el usuario se registre

from .constants import COUNTRY_CHOICES, MODALITY_CHOICES

# Create your models here.
class Company(models.Model):
    pass
    # is_company = models.BooleanField(default=True)
    # username = models.EmailField("Email", unique=True)
    # company_name = models.CharField("Nombre de la compañía", max_length=150, unique=True)
    # # email = models.EmailField("Email", unique=True)
    # password1 = models.CharField("Contraseña", max_length=20)
    # password2 = models.CharField("Repetir contraseña", max_length=20)
    # location = models.CharField("Ubicación", choices=COUNTRY_CHOICES, max_length=50)
    # phone = models.IntegerField("Teléfono", default=0, unique=True)
    # web = models.CharField("Página web", max_length=150, default='example.com', blank=True, unique=True)

    # def __str__(self) -> str:
    #     return f'{self.id}: {self.company_name}'
    
class Offer(models.Model):
    pass
    # title = models.CharField("Título", max_length=150)
    # description = models.CharField("Descripción", max_length=1000)
    # salary = models.IntegerField("Salario", default=0, blank=True)
    # modality = models.CharField("Modalidad", choices=MODALITY_CHOICES, max_length=50)
    # location = models.CharField("Ubicación", max_length=150)
    # company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    # def __str__(self) -> str:
    #     return f'{self.id}: {self.title}'

# ---- User ---

# upload directory
# instance: usuario
# filename: archivo que estamos subiendo
def user_directory_path_profile(instance, filename):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture_name
class User(AbstractUser):
    dni = models.IntegerField("DNI", default=0)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='profile')
    is_professional = models.BooleanField(default=True)

    # User info
    avatar = models.ImageField(default='users/user-default-profile.png', upload_to='user_directory_path_profile')
    bio = models.TextField(max_length=300, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    # cv = models.FileField()
    job_offer_id = models.ManyToManyField(Offer)

    def __str__(self) -> str:
        return self.user.username


# cuando el usuario se registra
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()

# crear el perfil del usuario
post_save.connect(create_user_profile, sender=User)
# guardar el perfil creado por el usuario
post_save.connect(save_user_profile, sender=User)