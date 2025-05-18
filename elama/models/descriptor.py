from django.db import models
from ckeditor.fields import RichTextField
from . import Principio


class Descriptor(models.Model):
    """
    Descriptor asociado a un principio, que forma parte de las estrategias educativas
    para el desarrollo de los Programas de ELAMA.

    Campos:
        - principio: referencia al principio al que pertenece el descriptor.
        - titulo: título del descriptor.
        - contenido_html: contenido enriquecido en formato HTML, puede estar vacío.
        - descriptor_padre: referencia a otro descriptor que actúa como padre (jerarquía).
        - step: entero para controlar el orden y paginación de los descriptores.

    Meta:
        verbose_name_plural: nombre plural para el modelo en la administración.

    Métodos:
        - __str__: devuelve el título como representación en string.
    """
    principio = models.ForeignKey(Principio, on_delete=models.CASCADE)  # Principio asociado
    titulo = models.CharField(max_length=200)  # Título del descriptor
    contenido_html = RichTextField(blank=True, null=True)  # Contenido enriquecido en HTML
    descriptor_padre = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)  # Descriptor padre opcional
    step = models.IntegerField(null=True)  # Orden y paginación

    class Meta:
        verbose_name_plural = 'descriptores'  # Nombre plural en admin

    def __str__(self):
        return self.titulo  # Representación del descriptor: su título
