from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from elama.models import Grupo, Autoevaluacion

@login_required
def grupal(request: HttpRequest):

    if request.method == 'POST':
        nuevo_grupo = Grupo(nombre=request.POST['nombre'])
        # Se hace responsable al usuario autenticado (La petición no devuelve el id de este)
        nuevo_grupo.responsable_id = request.user.id
        nuevo_grupo.save()

        # Recorremos los usuarios seleccionados
        for usuario_id in request.POST['ids']:
            # Creamos una autoevaluación individual por cada usuario seleccionado
            autoevaluacion_individual = Autoevaluacion(usuario_id=usuario_id, grupo_id=nuevo_grupo.id)
            autoevaluacion_individual.save()

        # Crear la evaluacion del usuario autenticado
        autoevaluacion_responsable = Autoevaluacion(usuario_id=request.user.id, grupo_id=nuevo_grupo.id)
        autoevaluacion_responsable.save()

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