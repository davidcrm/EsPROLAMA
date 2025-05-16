from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, FileResponse

from elama.forms.volcado_form import VolcadoForm
from elama.services.individual_service import IndividualService
from elama.models import Estrategia, Descriptor, Volcado, Autoevaluacion
from elama.services.pdf_service import PdfService


@login_required
def individual(request: HttpRequest):
    """
    Vista para mostrar la lista de autoevaluaciones individuales del usuario autenticado
    o crear una nueva autoevaluación al recibir POST.

    GET: Muestra las autoevaluaciones sin grupo del usuario.
    POST: Crea una nueva autoevaluación y redirige a su detalle.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.

    Returns:
        HttpResponse: Renderiza la plantilla con autoevaluaciones o redirige a detalle.
    """
    if request.method == 'POST':
        autoevaluacion = Autoevaluacion(usuario_id=request.user.id)
        autoevaluacion.save()
        return redirect('elama:individual-detail', autoevaluacion_id=autoevaluacion.id)

    autoevaluaciones = (Autoevaluacion.objects
                        .filter(usuario_id=request.user.id, grupo_id__isnull=True)
                        .order_by("fecha_hora"))
    return render(request, 'elama/individual.html', {
        'autoevaluaciones': autoevaluaciones
    })


@login_required
def detalle_individual(request: HttpRequest, autoevaluacion_id: int):
    """
    Muestra el detalle de una autoevaluación individual o grupal
    si el usuario es propietario o responsable del grupo.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.
        autoevaluacion_id (int): ID de la autoevaluación a mostrar.

    Returns:
        HttpResponse: Renderiza el detalle con estrategias y volcados.
    """
    autoevaluacion = Autoevaluacion.objects.filter(
        Q(pk=autoevaluacion_id),
        Q(usuario_id=request.user.id) | Q(grupo__responsable_id=request.user.id)
    ).get()

    estrategias = Estrategia.objects.prefetch_related('principio_set__descriptor_set').all()
    volcados = Volcado.objects.filter(autoevaluacion_id=autoevaluacion_id)

    # Define ruta de regreso dependiendo si es grupal o individual
    if autoevaluacion.grupo_id:
        ruta_home = reverse('elama:grupal')
    else:
        ruta_home = reverse('elama:individual')

    return render(request, 'elama/detalle_individual.html', {
        'autoevaluacion': autoevaluacion,
        'estrategias': estrategias,
        'volcados': volcados,
        'ruta_home': ruta_home
    })


@login_required
def individual_descriptor(request: HttpRequest, autoevaluacion_id: int, descriptor_id: int):
    """
    Vista para mostrar y editar un descriptor específico dentro de una autoevaluación.

    Permite navegar entre descriptores y guardar volcados asociados.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.
        autoevaluacion_id (int): ID de la autoevaluación.
        descriptor_id (int): ID del descriptor a mostrar.

    Returns:
        HttpResponse: Renderiza formulario para el descriptor o redirige según paginación.
    """
    individual_service = IndividualService()
    autoevaluacion = Autoevaluacion.objects.filter(
        Q(pk=autoevaluacion_id),
        Q(usuario_id=request.user.id) | Q(grupo__responsable_id=request.user.id)
    ).get()

    descriptor = Descriptor.objects.prefetch_related("principio__descriptor_set").get(pk=descriptor_id)
    paginacion = individual_service.paginacion(descriptor)

    if request.method == 'POST':
        individual_service.crear_volcado(
            data=request.POST,
            autoevaluacion=autoevaluacion,
            descriptor=descriptor
        )

        # Navega entre descriptores o vuelve al detalle cuando es el último
        if paginacion['ultimo_descriptor'].id != descriptor.id:
            if 'anterior' in request.POST:
                return redirect(
                    'elama:individual-descriptor',
                    autoevaluacion_id=autoevaluacion.id,
                    descriptor_id=paginacion['anterior_descriptor'].id
                )
            return redirect(
                'elama:individual-descriptor',
                autoevaluacion_id=autoevaluacion.id,
                descriptor_id=paginacion['siguiente_descriptor'].id
            )
        else:
            return redirect('elama:individual-detail', autoevaluacion_id=autoevaluacion.id)

    volcado = Volcado.objects.filter(
        autoevaluacion_id=autoevaluacion.id,
        descriptor_id=descriptor.id,
    ).first()

    # Carga el formulario con datos si existe el volcado, sino vacío
    form = VolcadoForm(instance=volcado) if volcado else VolcadoForm()

    # Deshabilita campos logro y mejora si la autoevaluación está finalizada
    if autoevaluacion.finalizada:
        form.fields['logro'].widget.attrs['disabled'] = True
        form.fields['mejora'].widget.attrs['disabled'] = True

    return render(request, 'elama/individual_descriptor.html', {
        'autoevaluacion': autoevaluacion,
        'descriptor': paginacion['siguiente_descriptor'] if request.method == 'POST' else descriptor,
        'form': form,
        **paginacion,
    })


@login_required
def finalizar_individual(request: HttpRequest, autoevaluacion_id: int):
    """
    Marca una autoevaluación como finalizada.

    Solo puede hacerlo el propietario o el responsable del grupo.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.
        autoevaluacion_id (int): ID de la autoevaluación a finalizar.

    Returns:
        HttpResponseRedirect: Redirige al detalle de la autoevaluación.
    """
    autoevaluacion = Autoevaluacion.objects.filter(
        Q(pk=autoevaluacion_id),
        Q(usuario_id=request.user.id) | Q(grupo__responsable_id=request.user.id)
    ).get()

    autoevaluacion.finalizada = True  # Marca como finalizada
    autoevaluacion.save()  # Guarda cambios

    return redirect('elama:individual-detail', autoevaluacion_id=autoevaluacion_id)


@login_required
def exportar(request: HttpRequest, autoevaluacion_id: int):
    """
    Genera y descarga un PDF con la autoevaluación individual.

    Solo accesible para propietario o responsable del grupo.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.
        autoevaluacion_id (int): ID de la autoevaluación a exportar.

    Returns:
        FileResponse: Respuesta con el archivo PDF adjunto.
    """
    autoevaluacion = Autoevaluacion.objects.filter(
        Q(pk=autoevaluacion_id),
        Q(usuario_id=request.user.id) | Q(grupo__responsable_id=request.user.id)
    ).get()

    pdf_file = PdfService.export_autoevaluacion_individual(autoevaluacion, request.user)
    return FileResponse(
        pdf_file,
        as_attachment=True,
        filename="autoevaluacion.pdf"
    )
