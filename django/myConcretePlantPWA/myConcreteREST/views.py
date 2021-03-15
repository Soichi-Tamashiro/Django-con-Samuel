from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import *

from .serializers import *

# Create your views here.


class MyConcrete_Data_Add(generics.CreateAPIView):
    queryset = myConcrete_Data.objects.all()
    serializer_class = myConcrete_Data_Serializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class myConcrete_Data_List(generics.ListCreateAPIView):
    queryset = myConcrete_Data.objects.all()
    serializer_class = myConcrete_Data_Serializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class myConcrete_Data_Detail(generics.ListCreateAPIView):
    queryset = myConcrete_Data.objects.all()
    serializer_class = myConcrete_Data_Serializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# class UserList(APIView):  # new
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(APIView):  # new
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
