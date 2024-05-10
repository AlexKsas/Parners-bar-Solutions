
from django.db import models
from django.contrib.auth.models import AbstractUser

#Modelos 

class Asistencia(models.Model):
    
    id = models.AutoField(primary_key=True)
    idEvento = models.CharField(max_length=15)
    idUsuario = models.CharField(max_length=15)
    fechaIngreso = models.DateField(max_length=45)

    def __str__(self):
        return f"{self.id} - {self.idEstablecimiento} - {self.idPersona}" 
    

class ListadoCanciones(models.Model):
    
    id = models.AutoField(primary_key=True)
    idEvento = models.CharField(max_length=15)
    idAsistencia = models.CharField(max_length=15)
    nombreCancion = models.CharField(max_length=300)
    artista = models.CharField(max_length=300)
    albun = models.CharField(max_length=300)
    duracion = models.CharField(max_length=300)
    linkFotoCancion = models.TextField()
    fechaSolicitada = models.DateField(max_length=45)
    estadoCancion = models.TextField()
    linkReproductor = models.TextField()
    

    def __str__(self):
        return f"{self.id} - {self.idEstablecimiento} - {self.idPersona}" 
    


class User(AbstractUser):
    
    cedula = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    tipoIdentificacion = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    imagen = models.TextField()
    fechaNacimiento = models.DateField()
    edad = models.CharField(max_length=15)
    genero = models.CharField(max_length=50)
    idEstablecimiento = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.cedula} - {self.celular}"
    
    

class eventos(models.Model):

    id = models.AutoField(primary_key=True)
    latitud = models.CharField(max_length=45)
    longitud = models.CharField(max_length=45)
    nombreEvento = models.CharField(max_length=45)
    cover = models.CharField(max_length=45)
    horarios = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    fechaInicio = models.DateField(max_length=45)
    fechaFin = models.DateField(max_length=45)
    habilitarCanciones = models.CharField(max_length=45)
    idEstablecimiento = models.CharField(max_length=45)
    imagen = models.TextField()

    def __str__(self):
        return f"{self.id}"
    
class MegustaEventos(models.Model):

    id = models.AutoField(primary_key=True)
    idEvento = models.CharField(max_length=45)
    idUsuario = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.id}"
    
class MegustaEstablecimiento(models.Model):

    id = models.AutoField(primary_key=True)
    idEstablecimiento = models.CharField(max_length=45)
    idUsuario = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.id}"
    
class Comentarios(models.Model):

    id = models.AutoField(primary_key=True)
    idEvento = models.CharField(max_length=45)
    idUsuario = models.CharField(max_length=45)
    comentario = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.id}"
    

class Productos(models.Model):

    id = models.AutoField(primary_key=True)
    idEstablecimiento = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    categoria = models.CharField(max_length=45)
    urlImagen = models.TextField()

    def __str__(self):
        return f"{self.id}"
    

    


