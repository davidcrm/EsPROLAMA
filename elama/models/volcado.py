from django.db import models
from . import Autoevaluacion, Descriptor

class Volcado(models.Model):
    """Valoración realizada a un descriptor en una autoevaluación."""
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)
    descriptor = models.ForeignKey(Descriptor, on_delete=models.CASCADE)
    valoracion = models.CharField(max_length=1)
    logro = models.CharField(max_length=255, null=True, blank=True)
    mejora =models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Descriptor: {self.descriptor_id} - Valoración: {self.valoracion}"
