from django.db import models


class Autoevaluacion(models.Model):
    """Datos propios a tener en cuenta de la autoevaluación."""
    fecha_hora = models.DateTimeField(auto_now_add=True)
    finalizada = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'autoevaluaciones'

    def __str__(self):
        return self.fecha_hora.isoformat()