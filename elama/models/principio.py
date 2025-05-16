from django.db import models
from . import Estrategia


class Principio(models.Model):
    """
    Principio perteneciente a una estrategia educativa para el desarrollo de Programas de ELAMA.

    Campos:
        - estrategia: clave foránea a Estrategia.
        - titulo: título del principio.
        - step: entero para paginación y orden, puede ser nulo.

    Métodos:
        - __str__: devuelve el título del principio.
    """
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    step = models.IntegerField(null=True)

    def __str__(self):
        return self.titulo
