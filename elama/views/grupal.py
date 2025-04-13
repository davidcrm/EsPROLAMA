from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from elama.models import Grupo, Autoevaluacion


@login_required
def grupal(request: HttpRequest):
    if request.method == 'POST':
        # TODO: Crear grupo y asignar el responsable
        # TODO: Crear las autoevaluaciones individuales para cada usuario,
        #  incluyendo el usuario autenticado que no viene en los datos del formulario
        print(f"/POST /grupal {request.POST}")


    usuario_autenticado = User.objects.get(pk=request.user.id)
    grupos_supervisados = Grupo.objects.filter(responsable_id=usuario_autenticado.id)
    grupales_no_supervisadas = (Autoevaluacion.objects
        .filter(
            usuario_id=usuario_autenticado.id,
            grupo_id__isnull=False,
        ).exclude(
            grupo__responsable_id=usuario_autenticado.id,
        )
    )
    usuarios = (User.objects
                .filter(is_superuser=False, is_staff=False)
                .exclude(id=usuario_autenticado.id))

    return render(request,
        'elama/grupal.html',
        {
            'grupos_supervisados': grupos_supervisados,
            'grupales_no_supervisadas': grupales_no_supervisadas,
            'usuarios': usuarios,
         }
    )