from django.contrib import admin
from .models import MO_project, MO_task

# Register your models here.
admin.site.register(MO_project)
admin.site.register(MO_task)
