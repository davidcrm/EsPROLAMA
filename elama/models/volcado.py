from django.db import models
from . import Autoevaluacion, Descriptor

class Volcado(models.Model):
    """
    Valoración asociada a un descriptor dentro de una autoevaluación.

    Campos:
        - autoevaluacion: clave foránea a Autoevaluacion.
        - descriptor: clave foránea a Descriptor.
        - valoracion: valor de la valoración, cadena de 1 carácter.
        - logro: texto opcional que indica un logro.
        - mejora: texto opcional que indica una mejora.

    Métodos:
        - __str__: devuelve una representación con el ID del descriptor y la valoración.
    """
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)
    descriptor = models.ForeignKey(Descriptor, on_delete=models.CASCADE)
    valoracion = models.CharField(max_length=1)
    logro = models.CharField(max_length=255, null=True, blank=True)
    mejora = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Descriptor: {self.descriptor_id} - Valoración: {self.valoracion}"
