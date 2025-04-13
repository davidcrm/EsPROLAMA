from django.http import HttpRequest
from django.shortcuts import render

from elama.models import Autoevaluacion

def mis_autoevaluaciones(request: HttpRequest):
    autoevaluaciones = (Autoevaluacion.objects
                        .filter(usuario_id=request.user.id, grupo_id__isnull=True)
                        .order_by("fecha_hora"))
    return render(request, 'elama/dashboard.html', {
        'autoevaluaciones': autoevaluaciones
    })
