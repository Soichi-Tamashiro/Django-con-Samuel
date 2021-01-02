# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myConcreteWeb import views

urlpatterns = [
    path("", views.myindex.as_view()),
    # path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
