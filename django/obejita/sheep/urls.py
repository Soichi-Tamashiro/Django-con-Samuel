
from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import ItemsView, ItemView

urlpatterns = [
    path('', sayHello, name='sayHello'),
    path('Books/', Books, name='Books'),
    path('Books/<int:bookid>', BookID, name='BookID'),
    path('items/', ItemsView),
    path('item/<int:nm>/', ItemView),
]
