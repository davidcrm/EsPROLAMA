from django.db import models


class Estrategia(models.Model):
    """
    Modelo que representa una estrategia educativa para el desarrollo de los
    Programas de ELAMA.

    Campos:
        - titulo: título descriptivo de la estrategia.
        - step: entero usado para ordenar y paginar las estrategias.

    Métodos:
        - __str__: devuelve el título como representación en string.
    """
    titulo = models.CharField(max_length=200)  # Título de la estrategia
    step = models.IntegerField(null=True)  # Orden y paginación

    def __str__(self):
        return self.titulo  # Representación: título de la estrategia
