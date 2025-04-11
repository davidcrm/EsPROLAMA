from django.db import models

from elama.models import Autoevaluacion
from elama.models.grupo import Grupo


class Grupo_autoevaluacion(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)