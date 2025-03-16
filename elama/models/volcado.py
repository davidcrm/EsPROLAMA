from django.db import models
from . import Autoevaluacion, Descriptor


class Volcado(models.Model):
    """Valoración realizada a un descriptor en una autoevaluación."""
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)
    descriptor = models.ForeignKey(Descriptor, on_delete=models.CASCADE)
    valoracion = models.CharField(max_length=1)

    def __str__(self):
        return f"Autoevaluación: {self.autoevaluacion} - Descriptor: {self.descriptor} - Valoración: {self.valoracion}"
