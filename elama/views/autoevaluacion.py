from django.shortcuts import render

from elama.models import Autoevaluacion

def mis_autoevaluaciones(request):
    autoevaluaciones = Autoevaluacion.objects.order_by("fecha_hora")
    return render(request, 'elama/dashboard.html', {
        'autoevaluaciones': autoevaluaciones
    })
