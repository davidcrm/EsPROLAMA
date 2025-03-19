from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from elama.forms import VolcadoForm
from elama.models import Autoevaluacion, Descriptor, Volcado

# Vista para volcar datos de una autoevaluación para un descriptor específico, solo accesible para usuarios autenticados.
@login_required
def volcar_autoevaluacion(request, id_autoevaluacion, id_descriptor):
    # Obtiene la autoevaluación y el descriptor.
    autoevaluacion = Autoevaluacion.objects.get(pk=id_autoevaluacion)
    descriptor = Descriptor.objects.get(pk=id_descriptor)
    valoracion = '-1'  # Valoración por defecto.
    existe = True  # Bandera para verificar si ya existe un volcado.

    # Intenta obtener el volcado existente para la autoevaluación y descriptor.
    try:
        volcado = Volcado.objects.get(autoevaluacion__id=id_autoevaluacion, descriptor__id=id_descriptor)
        valoracion = volcado.valoracion  # Si existe, se usa la valoración guardada.
    except ObjectDoesNotExist:
        existe = False  # Si no existe, se establece que no existe un volcado.

    # Si no es una solicitud POST, muestra el formulario con los datos actuales o vacíos.
    if request.method != 'POST':
        if existe:
            form = VolcadoForm(instance=volcado)  # Pre-llena el formulario si ya existe el volcado.
        else:
            form = VolcadoForm()  # Muestra un formulario vacío si no existe volcado.
    else:
        # Si es una solicitud POST, procesa el formulario con los datos enviados.
        if existe:
            form = VolcadoForm(instance=volcado, data=request.POST)
            if form.is_valid():  # Si el formulario es válido, guarda los cambios.
                volcado.save()
                return redirect('elama:individual', id_autoevaluacion=id_autoevaluacion)
        else:
            form = VolcadoForm(data=request.POST)
            if form.is_valid():  # Si el formulario es válido, guarda un nuevo volcado.
                nuevo_volcado = form.save(commit=False)
                nuevo_volcado.autoevaluacion = autoevaluacion
                nuevo_volcado.descriptor = descriptor
                nuevo_volcado.save()
                return redirect('elama:individual', id_autoevaluacion=id_autoevaluacion)

    # Prepara el contexto con los datos necesarios para renderizar la vista.
    context = {
        'autoevaluacion': autoevaluacion, 'descriptor': descriptor, 'valoracion': int(valoracion),
        'form': form, 'valores': [i for i in range(1, 5)]  # Valores para la valoración.
    }
    return render(request, 'elama/volcado.html', context)