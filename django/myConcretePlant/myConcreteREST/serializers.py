from rest_framework import serializers
from myConcreteREST.models import myConcrete_Data
from django.contrib.auth.models import User


class myConcrete_Data_Serializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = myConcrete_Data
        fields = (
            "id",
            "Lote",
            "Empresa",
            "Fecha",
            "Cantidad",
            "T_Producción",
            "RUC",
            "Cemento",
            "Agregado_1",
            "Agregado_2",
            "Agua",
            "Aditivo_1",
            "owner",
        )


class UserSerializer(serializers.ModelSerializer):
    myConcrete_Data = serializers.PrimaryKeyRelatedField(
        many=True, queryset=myConcrete_Data.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "myConcrete_Data")

