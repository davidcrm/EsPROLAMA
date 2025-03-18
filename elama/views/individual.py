from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from elama.models import Estrategia, Principio, Descriptor, Autoevaluacion, Volcado

# Vista que muestra los detalles de una autoevaluación específica, solo accesible para usuarios autenticados.
@login_required
def individual(request, id_autoevaluacion):
    # Obtiene las estrategias, principios y descriptores ordenados por título.
    estrategias = Estrategia.objects.order_by('titulo')
    principios = Principio.objects.order_by('titulo')
    descriptores = Descriptor.objects.order_by('titulo')
    # Obtiene la autoevaluación y los volcados relacionados.
    autoevaluacion = Autoevaluacion.objects.get(pk=id_autoevaluacion)
    volcados_autoevaluacion = Volcado.objects.filter(autoevaluacion__id=id_autoevaluacion).values_list('descriptor')
    v_a = [id[0] for id in volcados_autoevaluacion]  # Lista de ids de descriptores volcados.
    context = {
        'estrategias': estrategias, 'principios': principios, 'descriptores': descriptores,
        'autoevaluacion': autoevaluacion, 'volcados_autoevaluacion': v_a
    }
    return render(request, 'elama/individual.html', context)