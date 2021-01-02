from rest_framework import serializers
from .models import ItemsModel


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = ['id', 'name', 'price']
