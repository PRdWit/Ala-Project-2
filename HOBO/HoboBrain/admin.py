from django.contrib import admin
from django.apps import apps

# Import all models from your app
models = apps.get_models()

# Register all models with the admin interface
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
