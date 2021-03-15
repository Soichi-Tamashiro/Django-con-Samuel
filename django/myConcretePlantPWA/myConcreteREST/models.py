from django.db import models
import os
import random
import datetime

# Create your models here.


class myConcrete_Data(models.Model):
    def lote_string():
        valor = str(datetime.date.today()).replace("-", "") + "01"
        return valor

    lote = models.CharField(max_length=100, default=lote_string)
    empresa = models.CharField(max_length=200, blank=True, default="")
    fecha = models.DateField(null=True, auto_now_add=True, auto_now=False)
    hora = models.TimeField(null=True, auto_now_add=True, auto_now=False)
    cantidad = models.FloatField(blank=True)
    t_producción = models.TimeField(blank=True)
    ruc = models.CharField(max_length=11)
    cemento = models.FloatField()
    agregado_1 = models.FloatField()
    agregado_2 = models.FloatField()
    agua = models.IntegerField()
    aditivo_1 = models.IntegerField()
    # owner = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return str(self.id)  # Para almacenar con nombre por fechas

