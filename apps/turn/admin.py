from django.contrib import admin
from apps.turn.models import Turn

@admin.register(Turn)
class TurnAdmin(admin.ModelAdmin):
    list_display = ('client', 'barber', 'date', 'time')
    list_filter = ('client', 'barber', 'date')
    search_fields = ('client__name', 'barber__name', 'date', 'time')





