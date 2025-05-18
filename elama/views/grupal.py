from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, FileResponse
from django.shortcuts import render, redirect
from elama.models import Grupo, Autoevaluacion, Descriptor, Estrategia, Volcado
from elama.services.pdf_service import PdfService


@login_required
def grupal(request: HttpRequest):
    """
    Vista para gestionar grupos y autoevaluaciones grupales.

    - Si la petición es POST, crea un nuevo grupo con el usuario autenticado
      como responsable.
    - Crea una autoevaluación individual para cada usuario seleccionado y otra para el responsable.
    - Muestra los grupos supervisados por el usuario y autoevaluaciones grupales
      no supervisadas.
    - Muestra la lista de usuarios que pueden agregarse al grupo.

    Args:
        request (HttpRequest): La petición HTTP del usuario.

    Returns:
        HttpResponse: Renderiza la plantilla 'elama/grupal.html' con la información necesaria.
    """
    if request.method == 'POST':
        nuevo_grupo = Grupo(nombre=request.POST['nombre'])
        nuevo_grupo.responsable_id = request.user.id  # Usuario autenticado es responsable
        nuevo_grupo.save()

        # Crear autoevaluaciones individuales para cada usuario seleccionado
        for usuario_id in request.POST.getlist('ids'):
            autoevaluacion_individual = Autoevaluacion(usuario_id=usuario_id, grupo_id=nuevo_grupo.id)
            autoevaluacion_individual.save()

        # Crear autoevaluación para el responsable del grupo
        autoevaluacion_responsable = Autoevaluacion(usuario_id=request.user.id, grupo_id=nuevo_grupo.id)
        autoevaluacion_responsable.save()

    grupos_supervisados = Grupo.objects.filter(responsable_id=request.user.id)
    # Autoevaluaciones grupales donde el usuario está pero no es responsable
    grupales_no_supervisadas = (Autoevaluacion.objects
        .filter(usuario_id=request.user.id, grupo_id__isnull=False)
        .exclude(grupo__responsable_id=request.user.id))
    # Usuarios normales excepto el usuario autenticado
    usuarios = (User.objects
                .filter(is_superuser=False, is_staff=False)
                .exclude(id=request.user.id))

    return render(request, 'elama/grupal.html', {
        'grupos_supervisados': grupos_supervisados,
        'grupales_no_supervisadas': grupales_no_supervisadas,
        'usuarios': usuarios,
    })


@login_required
def grupal_preview(request: HttpRequest, grupo_id: int):
    """
    Vista para mostrar el resumen/previsualización de la autoevaluación grupal.

    - Verifica que el usuario autenticado sea responsable del grupo.
    - Calcula la valoración promedio de cada descriptor basado en las autoevaluaciones
      del grupo.
    - Permite descargar el resumen en PDF si se envía un POST.

    Args:
        request (HttpRequest): Petición HTTP.
        grupo_id (int): ID del grupo a visualizar.

    Returns:
        HttpResponse: Renderiza la plantilla con el detalle o devuelve el PDF.
    """
    grupo = Grupo.objects.get(pk=grupo_id)

    # Comprobar si el usuario es responsable y si hay autoevaluaciones
    if request.user.id != grupo.responsable_id or grupo.autoevaluacion_set.count() == 0:
        return redirect('elama:grupal')

    # Obtener estrategias con sus principios y descriptores para mostrar
    estrategias = Estrategia.objects.prefetch_related('principio_set__descriptor_set').all()
    # Autoevaluación del usuario autenticado en ese grupo (no guardada, solo para contexto)
    autoevaluacion = Autoevaluacion(usuario_id=request.user.id, grupo_id=grupo.id)

    volcados = []

    # Calcular valoración promedio de cada descriptor basado en las autoevaluaciones del grupo
    for descriptor in Descriptor.objects.all():
        descriptor_volcados = Volcado.objects.filter(autoevaluacion__grupo_id=grupo.id, descriptor_id=descriptor.id)
        total_volcados = descriptor_volcados.count()

        if total_volcados == 0:
            continue  # No hay valoraciones, saltar descriptor

        valoracion_promedio = round(sum(int(d.valoracion) for d in descriptor_volcados) / total_volcados)
        volcados.append(Volcado(descriptor=descriptor, valoracion=valoracion_promedio))

    if request.method == 'POST':
        pdf_file = PdfService.export_autoevaluacion_individual(autoevaluacion, request.user, volcados)
        return FileResponse(pdf_file, as_attachment=True, filename="autoevaluacion.pdf")

    return render(request, 'elama/detalle_grupal.html', {
        'autoevaluacion': autoevaluacion,
        'estrategias': estrategias,
        'volcados': volcados
    })
