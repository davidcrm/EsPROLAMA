from django.db import models

from elama.models import Autoevaluacion
from elama.models.grupo import Grupo


class GrupoAutoevaluacion(models.Model):
    """
    Modelo intermedio que relaciona un Grupo con una Autoevaluacion.

    Campos:
        - grupo: referencia a un objeto Grupo.
        - autoevaluacion: referencia a un objeto Autoevaluacion.
    """
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)
