from django.db import models


class Estrategia(models.Model):
    """Estrategia educativa para el desarrollo de Programas de ELAMA."""
    titulo = models.CharField(max_length=200)
    # Atributo para paginación y orden
    step = models.IntegerField()

    def __str__(self):
        return self.titulo