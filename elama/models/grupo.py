from django.contrib.auth.models import User
from django.db import models

class Grupo(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.nombre:
            return self.nombre
        return f"Grupo {self.id}"