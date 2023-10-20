from django.contrib import admin
from .models import Subject,Note

# Register your models here.

notes_models = [Subject,Note]

for model in notes_models:
    admin.site.register(model)
