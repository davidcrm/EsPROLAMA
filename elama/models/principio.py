from django.db import models
from . import Estrategia


class Principio(models.Model):
    """Principio de una de las estrategias educativas para el desarrollo de Programas de ELAMA."""
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
