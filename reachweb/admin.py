from django.contrib import admin

# Register your models here.
from .models import Chv, Patient, Emergencies, Location

admin.site.register(Chv)
admin.site.register(Patient)
admin.site.register(Emergencies)
admin.site.register(Location)
