from django.db import models
from .constants import COUNTRY_CHOICES

# Create your models here.
class Offer(models.Model):
    title = models.CharField(max_length=150)
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    # TODO: agregar campos del perfil completo de la otra form
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    job_offer_id = models.ManyToManyField(Offer)

    def __str__(self) -> str:
        return f'{self.id}: {self.lastname}, {self.name}'

class Company(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    company_name = models.CharField(max_length=150)
    location = models.CharField(choices=COUNTRY_CHOICES, max_length=50)
    phone = models.IntegerField(default=0)
    web = models.CharField(max_length=150, default='example.com')

    def __str__(self) -> str:
        return f'{self.id}: {self.lastname}, {self.name}'
