from django.db.models.query import QuerySet
from elama.models import Descriptor, Volcado
from django import template


register = template.Library()

@register.filter(name='descriptor_in_volcado')
def descriptor_in_volcado(descriptor: Descriptor, volcados: QuerySet[Volcado] | list[Volcado]):
    if type(volcados) == list:
        filtrado = list(filter(lambda v: v.descriptor_id == descriptor.id, volcados))
        return filtrado[0] if len(filtrado) > 0 else None
    return volcados.filter(descriptor_id=descriptor.id).first()

@register.filter(name='descriptor_contenido_vacio')
def descriptor_contenido_vacio(descriptor: Descriptor):
    return descriptor.contenido_html is None or len(descriptor.contenido_html.strip()) == 0

@register.filter(name='descriptor_identacion')
def descriptor_identacion(descriptor: Descriptor):
    titulo = descriptor.titulo.rstrip()
    if titulo.endswith('.'):
        puntos = titulo[:-1].count('.')
    else:
        puntos = titulo.count('.')

    padding_left = 16 if puntos > 2 else 0
    return  padding_left * puntos