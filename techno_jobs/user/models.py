from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    # TODO: agregar campos del perfil completo de la otra form

    def __str__(self) -> str:
        return self.username