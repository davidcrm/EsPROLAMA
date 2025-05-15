from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from admin_panel.forms.descriptor_form import DescriptorForm
from elama.models import Descriptor

links = [
    {'label': 'Dashboard', 'href': '/admin_panel/'},
    {'label': 'Usuarios', 'href': '/admin_panel/usuarios/'},
    {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
    {'label': 'Principios', 'href': '/admin_panel/principios/'},
    {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
]


@staff_member_required
def descriptor_list(request: HttpRequest):
    descriptores = Descriptor.objects.all().order_by('step')

    return render(request, 'admin_panel/descriptores_list.html', {
        'descriptores': descriptores,
        'links': links,
    })


# Vista para crear o editar un descriptor
@staff_member_required
def detalle_descriptor(request: HttpRequest, descriptor_id: int = None):
    descriptor = Descriptor.objects.get(pk=descriptor_id) if descriptor_id else None

    # Si el formulario se envía (POST)
    if request.method == 'POST':
        ultimo_descriptor = Descriptor.objects.filter(step__isnull=False).order_by('step').last()
        if ultimo_descriptor is None:
            return redirect('admin_panel:descriptores')

        body = request.POST.copy()

        if descriptor is None:
            body.update({'step': ultimo_descriptor.step + 1})

        form = DescriptorForm(body, instance=descriptor)  # Crea o actualiza

        if form.is_valid():
            form.save()  # Guarda los cambios o crea nuevo descriptor
            if not descriptor_id:  # Crear (descriptor no existe)
                return redirect('admin_panel:descriptores')
            # Actualizar datos de descriptor (descriptor existe)
            messages.success(request, '¡Descriptor actualizado con éxito!')

    else:
        form = DescriptorForm(instance=descriptor)  # Formulario vacío o con datos

    # Renderiza la plantilla de detalle (crear o editar) con el formulario y enlaces
    return render(request, 'admin_panel/detalle_descriptor.html', {
        'descriptor': descriptor,
        'form': form,
        'links': links
    })


# Vista para eliminar un descriptor (solo acepta POST)
@staff_member_required
@require_POST
def eliminar_descriptor(_, descriptor_id: int):
    descriptor = Descriptor.objects.get(pk=descriptor_id)  # Busca el descriptor
    if descriptor:
        descriptor.delete()  # Elimina de la base de datos
    return redirect('admin_panel:descriptores')  # Redirige a la lista de estrategias
