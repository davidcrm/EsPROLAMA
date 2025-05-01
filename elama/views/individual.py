from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse

from elama.forms.volcado_form import VolcadoForm

from elama.services.individual_service import IndividualService
from elama.models import Estrategia, Descriptor, Volcado

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, FileResponse
from elama.models import Autoevaluacion
from elama.services.pdf_service import PdfService


@login_required
def individual(request: HttpRequest):
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
    autoevaluacion = Autoevaluacion.objects.filter(
        Q(pk=autoevaluacion_id),
        Q(usuario_id=request.user.id) | Q(grupo__responsable_id=request.user.id)
    ).get()
    estrategias = Estrategia.objects.prefetch_related('principio_set__descriptor_set').all()
    volcados = Volcado.objects.filter(autoevaluacion_id=autoevaluacion_id)

    # Ruta para volver a home (depende si autoevaluación pertenece a grupo)
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

        if paginacion['ultimo_descriptor'].id != descriptor.id:
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

    # Si existe un volcado, se carga el formulario con los datos del volcado para poder editar
    if volcado is not None:
        form = VolcadoForm(instance=volcado)
    else:
        form = VolcadoForm()

    return render(request, 'elama/individual_descriptor.html', {
        'autoevaluacion': autoevaluacion,
        'descriptor': paginacion['siguiente_descriptor'] if request.method == 'POST' else descriptor,
        'form': form,
        **paginacion,
    })


# Vista para finalizar una autoevaluación, marcándola como finalizada.
@login_required
def finalizar_individual(request: HttpRequest, autoevaluacion_id: int):
    autoevaluacion = Autoevaluacion.objects.filter(
        Q(pk=autoevaluacion_id),
        Q(usuario_id=request.user.id) | Q(grupo__responsable_id=request.user.id)
    ).get()
    autoevaluacion.finalizada = True  # Marca la autoevaluación como finalizada.
    autoevaluacion.save()  # Guarda los cambios.

    return redirect('elama:individual-detail', autoevaluacion_id=autoevaluacion_id)  # Redirige a la vista individual.


@login_required
def exportar(request: HttpRequest, autoevaluacion_id: int):
    autoevaluacion = Autoevaluacion.objects.get(
        pk=autoevaluacion_id,
        usuario_id=request.user.id
    )
    pdf_file = PdfService.export_autoevaluacion_individual(autoevaluacion, request.user)
    return FileResponse(
        pdf_file,
        as_attachment=True,
        filename="autoevaluacion.pdf"
    )


