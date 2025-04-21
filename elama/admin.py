from django.contrib import admin
from .models import Estrategia, Principio, Descriptor, Autoevaluacion, Volcado
from .models.grupo import Grupo

# Register your models here.
admin.site.register(Estrategia)
admin.site.register(Principio)
admin.site.register(Descriptor)
admin.site.register(Grupo)


# SÓLO PARA TESTS EN LA FASE DE DESARROLLO.
admin.site.register(Autoevaluacion)
admin.site.register(Volcado)


