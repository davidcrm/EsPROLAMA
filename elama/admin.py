from django.contrib import admin
from .models import Estrategia, Principio, Descriptor, Autoevaluacion, Volcado

# Register your models here.
admin.site.register(Estrategia)
admin.site.register(Principio)
admin.site.register(Descriptor)

# SÓLO PARA TESTS EN LA FASE DE DESARROLLO.
admin.site.register(Autoevaluacion)
admin.site.register(Volcado)

