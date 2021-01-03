# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myConcreteWeb.views import myIndex
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = (
    [path("", myIndex),]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

urlpatterns = format_suffix_patterns(urlpatterns)

