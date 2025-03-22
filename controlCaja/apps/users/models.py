from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMINISTRADOR = 'administrador', 'Administrador'
        CAJA = 'caja', 'Caja'

    rol = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.CAJA
    )

    def __str__(self):
        return self.username
