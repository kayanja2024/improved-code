from django.contrib import admin
from .models import *
from .models import patiant_data
# Register your models here.


admin.site.register(Patient)
admin.site.register(Ambulance)
admin.site.register(Doctor)
admin.site.register(Bed)
admin.site.register(patiant_data)
admin.site.register(score)