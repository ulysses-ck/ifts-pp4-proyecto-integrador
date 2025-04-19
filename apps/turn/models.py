from django.db import models
from apps.client.models import Client
from apps.barber.models import Barber

class Turn(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.client.name} con {self.barber.name} el {self.date} a las {self.time}"