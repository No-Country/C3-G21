from django.db import models

from .constants import COUNTRY_CHOICES, MODALITY_CHOICES

# Create your models here.
class Company(models.Model):
    is_company = models.BooleanField(default=True)
    # username = models.CharField(max_length=30)
    company_name = models.CharField("Nombre de la compañía", max_length=150, unique=True)
    email = models.EmailField("Email", unique=True)
    password1 = models.CharField("Contraseña", max_length=20)
    password2 = models.CharField("Repetir contraseña", max_length=20)
    location = models.CharField("Ubicación", choices=COUNTRY_CHOICES, max_length=50)
    phone = models.IntegerField("Teléfono", default=0, unique=True)
    web = models.CharField("Página web", max_length=150, default='example.com', blank=True, unique=True)

    def __str__(self) -> str:
        return f'{self.id}: {self.company_name}'

class Offer(models.Model):
    title = models.CharField("Título", max_length=150)
    description = models.CharField("Descripción", max_length=1000)
    salary = models.IntegerField("Salario", default=0, blank=True)
    modality = models.CharField("Modalidad", choices=MODALITY_CHOICES, max_length=50)
    location = models.CharField("Ubicación", max_length=150)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id}: {self.title}'
class User(models.Model):
    is_professional = models.BooleanField(default=True)
    # username = models.CharField(max_length=30)
    name = models.CharField("Nombre", max_length=30)
    lastname = models.CharField("Apellido", max_length=30)
    email = models.EmailField("Email", unique=True)
    password1 = models.CharField("Contraseña", max_length=20)
    password2 = models.CharField("Repetir contraseña", max_length=20)
    # TODO: agregar campos del perfil completo de la otra form
    cv = models.FileField(required=True)
    job_offer_id = models.ManyToManyField(Offer)

    def __str__(self) -> str:
        return f'{self.id}: {self.lastname}, {self.name}'