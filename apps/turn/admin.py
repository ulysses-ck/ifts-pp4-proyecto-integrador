from django.contrib import admin
from apps.turn.models import TimeSlot, Turn

@admin.register(Turn)
class TurnAdmin(admin.ModelAdmin):
    list_display = ('client', 'barber', 'date', 'time_slot')
    list_filter = ('client', 'barber', 'date')
    search_fields = ('client__name', 'barber__name', 'date', 'time_slot')

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'end_time', 'is_active']
    list_filter = ['is_active']
    ordering = ['start_time']