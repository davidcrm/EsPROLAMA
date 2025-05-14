from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from admin_panel.forms.principio_form import PrincipioForm
from elama.models import Principio

links = [
    {'label': 'Dashboard', 'href': '/admin_panel/'},
    {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
    {'label': 'Principios', 'href': '/admin_panel/principios/'},
    {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
    {'label': 'Usuarios', 'href': '/admin_panel/usuarios/'},
]


@staff_member_required
def principios_list(request: HttpRequest):
    principios = Principio.objects.all().order_by('step')

    return render(request, 'admin_panel/principios_list.html', {
        'principios': principios,
        'links': links,
    })


@staff_member_required
def detalle_principio(request: HttpRequest, principio_id: int = None):
    principio = Principio.objects.get(pk=principio_id) if principio_id else None

    # Si el formulario se envía (POST)
    if request.method == 'POST':
        form = PrincipioForm(request.POST, instance=principio)  # Crea o actualiza
        form.save()  # Guarda los cambios o crea nuevo principio

        if not principio_id:  # Crear principio (principio no existe)
            return redirect('admin_panel:principios')
        # Actualizar datos de principio (principio existe)
        messages.success(request, '¡Principio actualizado con éxito!')

    else:
        form = PrincipioForm(instance=principio)  # Formulario vacío o con datos

    # Renderiza la plantilla de detalle (crear o editar) con el formulario y enlaces
    return render(request, 'admin_panel/detalle_principio.html', {
        'principio': principio,
        'form': form,
        'links': links
    })


@staff_member_required
@require_POST
def eliminar_principio(_, principio_id: int):
    principio = Principio.objects.get(pk=principio_id)  # Busca el principio
    if principio:
        principio.delete()  # Elimina de la base de datos
    return redirect('admin_panel:principios')  # Redirige a la lista de principios
