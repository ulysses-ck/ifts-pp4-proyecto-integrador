
from django.db import models
from apps.client.models import Client
from apps.barber.models import Barber


class TimeSlot(models.Model):
    """Modelo para definir los horarios disponibles de la barbería"""
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['start_time']
    
    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"
    

class Turn(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False, null=True)

    class Meta:
        unique_together = ['barber', 'date', 'time_slot', 'is_confirmed']

    def __str__(self):
        return f"{self.client.name} con {self.barber.name} el {self.date} a las {self.time_slot} ({self.is_confirmed})"