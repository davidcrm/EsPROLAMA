from django.db.models.functions import Trim
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from elama.services.individual_service import IndividualService
from elama.models import Estrategia, Principio, Descriptor, Autoevaluacion, Volcado
from elama.forms import VolcadoForm
@login_required
def crear_individual(request: HttpRequest):
    autoevaluacion = Autoevaluacion(usuario_id=request.user.id)  # Crea una nueva instancia de Autoevaluacion.
    autoevaluacion.save()  # Guarda la autoevaluación en la base de datos.
    return redirect('elama:individual', autoevaluacion_id=autoevaluacion.id)

@login_required
def nuevo_individual(request: HttpRequest, autoevaluacion_id: int):
    autoevaluacion = Autoevaluacion.objects.get(autoevaluacion_id=autoevaluacion_id, usuario_id=request.user.id)
    estrategias = Estrategia.objects.prefetch_related('principio_set__descriptor_set').all()

    return render(request, 'elama/individual.html', {
        'autoevaluacion': autoevaluacion,
        'estrategias': estrategias,
    })

@login_required
def individual_descriptor(request: HttpRequest, autoevaluacion_id: int, descriptor_id: int):
    individual_service = IndividualService()
    autoevaluacion = Autoevaluacion.objects.get(autoevaluacion_id=autoevaluacion_id, usuario_id=request.user.id)
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
            return redirect('elama:individual', autoevaluacion_id=autoevaluacion.id)


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
    autoevaluacion = Autoevaluacion.objects.get(pk=autoevaluacion_id, usuario_id=request.user.id)

    autoevaluacion.finalizada = True  # Marca la autoevaluación como finalizada.
    autoevaluacion.save()  # Guarda los cambios.

    return redirect('elama:individual', autoevaluacion_id=autoevaluacion_id)  # Redirige a la vista individual.
