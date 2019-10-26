from django.contrib import admin
from .models import RegistrationDetails


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number', 'gender')


admin.site.register(RegistrationDetails, RegistrationAdmin)
