from django.db import models


class DatosFamilia(models.Model):
    name = models.CharField(max_length=55)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.IntegerField