from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myConcreteREST.views import *

urlpatterns = [
    path("movicreto/add", MyConcrete_Data_Add.as_view()),  # POST
    path(
        "movicreto/detail/<int:pk>", myConcrete_Data_Detail.as_view()
    ),  # GET no se usara
    path("movicreto/list/", myConcrete_Data_List.as_view()),  # no se usara
]
urlpatterns = format_suffix_patterns(urlpatterns)
