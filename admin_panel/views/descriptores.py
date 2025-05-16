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
    """
    Vista protegida que muestra la lista de descriptores ordenados por su campo `step`.

    Solo accesible a usuarios con permisos de staff.

    Args:
        request (HttpRequest): Objeto HttpRequest de la petición entrante.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'admin_panel/descriptores_list.html'
        mostrando la lista de descriptores y los enlaces de navegación.
    """
    descriptores = Descriptor.objects.all().order_by('step')

    return render(request, 'admin_panel/descriptores_list.html', {
        'descriptores': descriptores,
        'links': links,
    })


@staff_member_required
def detalle_descriptor(request: HttpRequest, descriptor_id: int = None):
    """
    Vista protegida para crear o editar un descriptor.

    Si se recibe un descriptor_id, se edita el descriptor correspondiente.
    Si no, se crea uno nuevo asignando el siguiente valor de `step`.

    Solo accesible a usuarios con permisos de staff.

    Args:
        request (HttpRequest): Objeto HttpRequest de la petición entrante.
        descriptor_id (int, optional): ID del descriptor a editar. Por defecto None (crear).

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'admin_panel/detalle_descriptor.html'
        mostrando el formulario de edición o creación.
    """
    descriptor = Descriptor.objects.get(pk=descriptor_id) if descriptor_id else None

    if request.method == 'POST':
        ultimo_descriptor = Descriptor.objects.filter(step__isnull=False).order_by('step').last()
        if ultimo_descriptor is None:
            return redirect('admin_panel:descriptores')

        body = request.POST.copy()

        if descriptor is None:
            body.update({'step': ultimo_descriptor.step + 1})

        form = DescriptorForm(body, instance=descriptor)

        if form.is_valid():
            form.save()
            if not descriptor_id:
                return redirect('admin_panel:descriptores')
            messages.success(request, '¡Descriptor actualizado con éxito!')

    else:
        form = DescriptorForm(instance=descriptor)

    return render(request, 'admin_panel/detalle_descriptor.html', {
        'descriptor': descriptor,
        'form': form,
        'links': links
    })


@staff_member_required
@require_POST
def eliminar_descriptor(_, descriptor_id: int):
    """
    Vista protegida para eliminar un descriptor.

    Solo acepta peticiones POST y requiere permisos de staff.

    Args:
        _ (HttpRequest): Objeto HttpRequest (no se usa).
        descriptor_id (int): ID del descriptor a eliminar.

    Returns:
        HttpResponseRedirect: Redirige a la lista de descriptores tras eliminar.
    """
    descriptor = Descriptor.objects.get(pk=descriptor_id)
    if descriptor:
        descriptor.delete()
    return redirect('admin_panel:descriptores')
