from django.contrib.auth.models import User
from django.db import models

from elama.models.grupo import Grupo


class Autoevaluacion(models.Model):
    """Datos propios a tener en cuenta de la autoevaluación."""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    finalizada = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'autoevaluaciones'

    def __str__(self):
        return self.fecha_hora.isoformat()