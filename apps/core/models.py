from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('dueno', 'Dueño'),
        ('barbero', 'Barbero'),
        ('cliente', 'Cliente'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='cliente')

    def __str__(self):
        return f"{self.username} ({self.role})"
    

