from django.contrib import admin
from .models import Department, Job, HiredEmployee

admin.site.register(Department)
admin.site.register(Job)
admin.site.register(HiredEmployee)
