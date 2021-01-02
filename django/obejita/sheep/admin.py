from django.contrib import admin
from django.apps import apps
from .models import ItemsModel
# all other models
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
try:
    admin.site.register(ItemsModel)
except admin.sites.AlreadyRegistered:
    pass
