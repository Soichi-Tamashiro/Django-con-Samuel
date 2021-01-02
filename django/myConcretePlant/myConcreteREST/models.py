from django.db import models

# Create your models here.


class myConcrete_Data(models.Model):
    created = models.DateTimeField(auto_now=True)
    Fecha = models.DateTimeField(auto_now_add=True, blank=True)
    Cantidad = models.FloatField()
    Empresa = models.CharField(max_length=200, blank=True, default="")
    RUC = models.IntegerField()
    Cemento = models.FloatField()
    Agregado_1 = models.FloatField()
    Agregado_2 = models.FloatField()
    Agua = models.IntegerField()
    Aditivo_1 = models.IntegerField()
    T_Producción = models.TimeField()

    class Meta:
        ordering = ["created"]  # Para ordenarlo por fechas

    def __str__(self):
        return self.Fecha  # Para almacenar con nombre por fechas

