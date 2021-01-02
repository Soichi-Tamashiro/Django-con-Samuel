from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myConcreteREST import views

urlpatterns = [
    path("myConcreteREST/", views.myConcrete_Data_List.as_view()),
    path("myConcreteREST/<int:pk>/", views.UserList.as_view()),
    path("user/", views.UserList.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
