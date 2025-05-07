from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from admin_panel.forms.descriptor_form import DescriptorForm
from elama.models import Descriptor


@staff_member_required
def descriptor_list(request: HttpRequest):
    links = [
        {'label': 'Dashboard', 'href': '/admin_panel/'},
        {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
        {'label': 'Principios', 'href': '/admin_panel/principios/'},
        {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
    ]
    descriptores = Descriptor.objects.all().order_by('step')

    return render(request,'admin_panel/descriptores_list.html',{
        'descriptores':descriptores,
        'links': links,
    })


# Vista para crear o editar un descriptor
@staff_member_required
def detalle_descriptor(request: HttpRequest, descriptor_id: int = None):
    # Enlaces de navegación del panel de administración
    links = [
        {'label': 'Dashboard', 'href': '/admin_panel/'},
        {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
        {'label': 'Principios', 'href': '/admin_panel/principios/'},
        {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
    ]

    descriptor = None
    # Si se recibe un ID, busca la descriptor a editar
    if descriptor_id:
        descriptor = Descriptor.objects.get(pk=descriptor_id)

    # Si el formulario se envía (POST)
    if request.method == 'POST':
        form = DescriptorForm(request.POST, instance=descriptor)  # Crea o actualiza
        if form.is_valid():
            form.save()  # Guarda los cambios o crea nueva descriptor
            return redirect('admin_panel:descriptores')  # Redirige a la lista
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
def eliminar_descriptor(request: HttpRequest,descriptor_id: int):
    descriptor = Descriptor.objects.get(pk=descriptor_id)  # Busca el descriptor
    descriptor.delete()  # Elimina de la base de datos
    return redirect('admin_panel:descriptores')  # Redirige a la lista de estrategias