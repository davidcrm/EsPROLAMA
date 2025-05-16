from django.db.models.query import QuerySet
from elama.models import Descriptor, Volcado
from django import template

from elama.services.individual_service import IndividualService

register = template.Library()

@register.filter(name='descriptor_in_volcado')
def descriptor_in_volcado(descriptor: Descriptor, volcados: QuerySet[Volcado] | list[Volcado]):
    """
    Busca un Volcado relacionado con un Descriptor específico en una lista o queryset de volcados.

    Args:
        descriptor (Descriptor): Descriptor que se quiere encontrar en los volcados.
        volcados (QuerySet | list): Conjunto o lista de objetos Volcado.

    Returns:
        Volcado | None: El primer Volcado que coincide con el descriptor o None si no existe.
    """
    # Si volcados es lista, filtrar manualmente
    if type(volcados) == list:
        filtrado = list(filter(lambda v: v.descriptor_id == descriptor.id, volcados))
        return filtrado[0] if len(filtrado) > 0 else None

    # Si es queryset, usar filtro de Django
    return volcados.filter(descriptor_id=descriptor.id).first()


@register.filter(name='descriptor_contenido_vacio')
def descriptor_contenido_vacio(descriptor: Descriptor):
    """
    Comprueba si el contenido HTML de un descriptor está vacío usando el servicio IndividualService.

    Args:
        descriptor (Descriptor): Descriptor a comprobar.

    Returns:
        bool: True si el contenido está vacío o None, False en caso contrario.
    """
    return IndividualService().contenido_html_vacio(descriptor)


@register.filter(name='descriptor_identacion')
def descriptor_identacion(descriptor: Descriptor):
    """
    Calcula la indentación (padding-left en px) que debería aplicarse al descriptor en función
    de la cantidad de puntos en su título.

    Args:
        descriptor (Descriptor): Descriptor cuyo título se analiza.

    Returns:
        int: Padding left calculado para indentación.
    """
    titulo = descriptor.titulo.rstrip()
    # Cuenta puntos en el título para determinar nivel
    if titulo.endswith('.'):
        puntos = titulo[:-1].count('.')
    else:
        puntos = titulo.count('.')

    padding_left = 16 if puntos > 2 else 0
    return padding_left * puntos
