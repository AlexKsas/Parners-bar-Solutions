
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Asistencia(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    idEstablecimiento = models.CharField(max_length=10)
    idPersona = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.id} - {self.idEstablecimiento} - {self.idPersona}" 
    


class User(AbstractUser):
    
    cedula = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)



