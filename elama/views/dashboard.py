from django.shortcuts import render

from elama.models import Autoevaluacion


def dashboard(request):
    autoevaluaciones = Autoevaluacion.objects.order_by("fecha_hora")
    context = {
        'autoevaluaciones': autoevaluaciones
    }
    return render(request,'elama/dashboard.html',context)