from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render

from elama.models import Autoevaluacion
from elama.models.grupo import Grupo


@login_required
def crear_grupal(request:HttpRequest):
    usuario_autenticado = User.objects.get(pk=request.user.id)
    grupos = Grupo.objects.filter(responsable_id=usuario_autenticado.id)


    return render(request,
        'elama/grupal.html',
        {
            'grupos': grupos,

         }
    )