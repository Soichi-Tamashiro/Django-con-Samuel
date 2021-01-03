from django.urls import include, path
from myConcrete_Accounts.views import ListUsers, CustomAuthToken

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),  # log rest
    path("api/users/", ListUsers.as_view()),
    path("api/token/auth/", CustomAuthToken.as_view()),
]
