from django.db import models
# from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save # una señal, lo que ocurrira cuando el usuario se registre
from django.contrib.auth.validators import UnicodeUsernameValidator

from .constants import COUNTRY_CHOICES, MODALITY_CHOICES

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)

# ---- Company ----
class CompanyProfile(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    id = models.AutoField(primary_key=True)
    username = models.CharField(
        ("username"),
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )
    email = models.EmailField(blank=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["username", 'email']
    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
# class CompanyProfile(models.Model):
#     user = models.OneToOneField(Company, primary_key=True, on_delete=models.CASCADE, related_name='company')
    is_company = models.BooleanField(default=True)

    # Company Info
    logo = models.ImageField(default='company/company-default-logo.png', upload_to='user_directory_path_logo')
    company_name = models.CharField(max_length=150, unique=True)
    bio = models.TextField(max_length=300, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    web = models.CharField(max_length=150, blank=True, unique=True)

    def __str__(self) -> str:
        return self.username

# # cuando la compañia se registra
# def create_company_profile(sender, instance, created, **kwargs):
#     if created:
#         CompanyProfile.objects.create(user=instance)

# def save_company_profile(sender, instance, created, **kwargs):
#     instance.profile.save()

# # crear el perfil del usuario
# post_save.connect(create_company_profile, sender=User)
# # guardar el perfil creado por el usuario
# post_save.connect(save_company_profile, sender=User)

# upload directory
# instance: usuario
# filename: archivo que estamos subiendo
def user_directory_path_logo(instance, filename):
    logo_picture_name = '/offer/{0}/logo.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, logo_picture_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return logo_picture_name
    
class Offer(models.Model):
    title = models.CharField("Título", max_length=150)
    logo = models.ImageField(default='offer/offer-default-logo.png', upload_to='user_directory_path_logo')
    company = models.CharField("Compañia", max_length=150)
    description = models.CharField("Descripción", max_length=2000)
    salary = models.IntegerField("Salario", default=0, blank=True)
    modality = models.CharField("Modalidad", choices=MODALITY_CHOICES, max_length=50)
    location = models.CharField("Ubicación", max_length=150)
    # company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id}: {self.title}, {self.company}'

# ---- User ---

# upload directory
# instance: usuario
# filename: archivo que estamos subiendo
def user_directory_path_profile(instance, filename):
    profile_picture_name = '/users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture_name

# upload cv
def user_directory_path_profile_cv(instance, filename):
    profile_cv_name = 'users/{0}/cv.pdf'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_cv_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_cv_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='profile')
    is_professional = models.BooleanField(default=True)

    # User info
    avatar = models.ImageField(default='users/user-default-profile.png', upload_to='user_directory_path_profile')
    bio = models.TextField(max_length=300, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    cv = models.FileField(blank=True, upload_to='user_directory_path_profile_cv')
    job_offer_id = models.ManyToManyField(Offer, blank=True)
    # offer_id = models.CharField(max_length=1000, null=True, blank=True)

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