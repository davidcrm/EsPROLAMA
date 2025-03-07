from django.db import models

# Create your models here.
class Estrategia(models.Model):
    """Estrategia educativa para el desarrollo de Programas de ELAMA."""
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Principio(models.Model):
    """Principio de una de las estrategias educativas para el desarrollo de Programas de ELAMA."""
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Descriptor(models.Model):
    """Descriptor de uno de los principios perteneciente a una de las estrategias educativas para el desarrollo de
       Programas de ELAMA."""
    principio = models.ForeignKey(Principio, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido_html = models.TextField(blank=True, null=True)
    descriptor_padre = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'descriptores'

    def __str__(self):
        return self.titulo

class Autoevaluacion(models.Model):
    """Datos propios a tener en cuenta de la autoevaluación."""
    fecha_hora = models.DateTimeField(auto_now_add=True)
    finalizada = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'autoevaluaciones'

    def __str__(self):
        return self.fecha_hora.isoformat()

class Volcado(models.Model):
    """Valoración realizada a un descriptor en una autoevaluación."""
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)
    descriptor = models.ForeignKey(Descriptor, on_delete=models.CASCADE)
    valoracion = models.CharField(max_length=1)

    def __str__(self):
        return f"Autoevaluación: {self.autoevaluacion} - Descriptor: {self.descriptor} - Valoración: {self.valoracion}"
