from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    nacimiento = models.DateField()
    def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.nacimiento}, {self.id}"

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    def __str__(self):
      return f"{self.nombre}, {self.raza}, {self.edad}, {self.id}"

class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.color}, {self.id}"




