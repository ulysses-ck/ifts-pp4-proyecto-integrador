from django.contrib import admin
from apps.barber.models import Barber

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
