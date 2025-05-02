from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLES= (
        ('dueno', 'Dueño'),
        ('cliente', 'Cliente'),
    )
    role = models.CharField(max_length=10, choices=ROLES)

    def __str__(self):
        return f"{self.username} {self.role} " #self.username