from django.contrib.auth.models import User
from django.db import models

class Grupo(models.Model):
    """
    Representa un grupo en el sistema.

    Campos:
        - nombre: nombre del grupo (opcional).
        - responsable: usuario responsable del grupo.

    Métodos:
        - __str__: devuelve el nombre si existe y no está vacío;
          si no, devuelve 'Grupo <id>'.
    """
    nombre = models.CharField(max_length=100, null=True, blank=True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.nombre and len(self.nombre.strip()) > 0:
            return self.nombre
        return f"Grupo {self.id}"
