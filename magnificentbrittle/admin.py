from django.contrib import admin
from .models import Patients, Records, Professionals, Assistant, Consultation

admin.site.register(Patients)
admin.site.register(Records)
admin.site.register(Professionals)
admin.site.register(Assistant)
admin.site.register(Consultation)