from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, FileResponse
from django.shortcuts import render, redirect
from elama.models import Grupo, Autoevaluacion, Descriptor, Estrategia, Volcado
from elama.services.pdf_service import PdfService


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

@login_required
def grupal_preview(request: HttpRequest, grupo_id: int):
    # Obtenemos el grupo correspondiente
    grupo = Grupo.objects.get(pk=grupo_id)

    # Si el usuario que hace la petición no es responsable del grupo, se le redirige a grupal
    if request.user.id != grupo.responsable_id or grupo.autoevaluacion_set.count() == 0:
        return redirect('elama:grupal')

    # Recogemos las estrategias, todos sus principios y sus descriptores
    estrategias = Estrategia.objects.prefetch_related('principio_set__descriptor_set').all()
    # Obtenemos la autoevaluación del usuario autenticado y el grupo solicitado
    autoevaluacion = Autoevaluacion(usuario_id=request.user.id, grupo_id=grupo.id)
    # Creamos una lista de volcados vacía para almacenar los promedios de cada evaluación
    volcados = []

    # Recorremos todos los descriptores
    for descriptor in Descriptor.objects.all():
        # Obtenemos todos los volcados de ese descriptor que sean de las autoevaluaciones que pertenecen al grupo
        descriptor_volcados = Volcado.objects.filter(autoevaluacion__grupo_id=grupo.id, descriptor_id=descriptor.id)
        # Contamos los volcados que hay en la autoevaluación
        total_volcados = descriptor_volcados.count()

        # Si no hay volcados pasa a la siguiente iteración del bucle
        if total_volcados == 0:
            continue

        # Calculamos la valoracion promedia de todos los volcados existentes para ese descriptor (en la autoevaluación)
        valoracion_promedio = round(sum(map(lambda d: int(d.valoracion), descriptor_volcados)) / total_volcados)
        # Añadimos un nuevo volcado a la lista con el descriptor correspondiente y el valor promedio
        volcados.append(Volcado(descriptor=descriptor, valoracion=valoracion_promedio))

    return render(request, 'elama/detalle_grupal.html', {
        'autoevaluacion': autoevaluacion,
        'estrategias': estrategias,
        'volcados': volcados
    })
