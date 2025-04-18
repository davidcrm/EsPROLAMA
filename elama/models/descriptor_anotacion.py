from django.db import models

from elama.models import Autoevaluacion, Descriptor


class DescriptorAnotacion(models.Model):
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)
    descriptor = models.ForeignKey(Descriptor, on_delete=models.CASCADE)
    logro = models.CharField(max_length=200, null=True, blank=True)
    mejora = models.CharField(max_length=200,null=True, blank=True)

