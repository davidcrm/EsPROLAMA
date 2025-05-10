from django.db import models
from ckeditor.fields import RichTextField
from . import Principio


class Descriptor(models.Model):
    """Descriptor de uno de los principios perteneciente a una de las estrategias educativas para el desarrollo de
       Programas de ELAMA."""
    principio = models.ForeignKey(Principio, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido_html = RichTextField(blank=True, null=True)
    descriptor_padre = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    # Atributo para paginación y orden
    step = models.IntegerField(null=True)


    class Meta:
        verbose_name_plural = 'descriptores'

    def __str__(self):
        return self.titulo