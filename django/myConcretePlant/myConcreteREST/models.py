from django.db import models

# Create your models here.


class myConcrete_Data(models.Model):
    created = models.DateTimeField(auto_now=True)
    Lote = models.CharField(max_length=100, blank=True, default="")
    Empresa = models.CharField(max_length=200, blank=True, default="")
    Fecha = models.CharField(max_length=100, blank=True, default="")
    Cantidad = models.FloatField()
    T_Producción = models.TimeField()
    RUC = models.IntegerField()
    Cemento = models.FloatField()
    Agregado_1 = models.FloatField()
    Agregado_2 = models.FloatField()
    Agua = models.IntegerField()
    Aditivo_1 = models.IntegerField()
    owner = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["created"]  # Para ordenarlo por fechas

    def __str__(self):
        return self.Fecha  # Para almacenar con nombre por fechas

