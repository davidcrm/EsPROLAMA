from django.contrib.auth.models import User
from django.db import models

from elama.models.grupo import Grupo


class Autoevaluacion(models.Model):
    """
    Modelo que representa una autoevaluación realizada por un usuario.

    Campos:
        - usuario: referencia al usuario que realiza la autoevaluación.
        - grupo: referencia opcional al grupo asociado.
        - fecha_hora: fecha y hora de creación, se establece automáticamente.
        - finalizada: indica si la autoevaluación está completada o no.

    Meta:
        verbose_name_plural: nombre plural para el modelo en la administración.

    Métodos:
        - __str__: devuelve la representación en string con la fecha y hora en formato ISO.
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que realiza la autoevaluación
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True)  # Grupo opcional asociado
    fecha_hora = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación automática
    finalizada = models.BooleanField(default=False)  # Estado de finalización de la autoevaluación

    class Meta:
        verbose_name_plural = 'autoevaluaciones'  # Nombre plural en el admin

    def __str__(self):
        return self.fecha_hora.isoformat()  # Representación del objeto: fecha y hora ISO
