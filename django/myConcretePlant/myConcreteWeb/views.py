# from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class myindex(TemplateView):
    template_name = "Index.html"
