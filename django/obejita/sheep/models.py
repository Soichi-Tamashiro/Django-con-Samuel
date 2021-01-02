from django.db import models

# Create your models here.


class ItemsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=False)
    price = models.IntegerField

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}:{self.price}"
