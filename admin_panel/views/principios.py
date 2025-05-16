from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from admin_panel.forms.principio_form import PrincipioForm
from elama.models import Principio

links = [
    {'label': 'Dashboard', 'href': '/admin_panel/'},
    {'label': 'Usuarios', 'href': '/admin_panel/usuarios/'},
    {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
    {'label': 'Principios', 'href': '/admin_panel/principios/'},
    {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
]


@staff_member_required
def principios_list(request: HttpRequest):
    """
    Obtiene y muestra la lista de todos los principios ordenados por 'step'.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.

    Returns:
        HttpResponse: Renderiza la plantilla 'admin_panel/principios_list.html'
                      con los principios y enlaces de navegación.
    """
    principios = Principio.objects.all().order_by('step')

    return render(request, 'admin_panel/principios_list.html', {
        'principios': principios,
        'links': links,
    })


@staff_member_required
def detalle_principio(request: HttpRequest, principio_id: int = None):
    """
    Vista para crear o editar un principio.

    Si se proporciona un principio_id, edita el principio correspondiente.
    Si no, crea uno nuevo.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.
        principio_id (int, opcional): ID del principio a editar. Por defecto None.

    Returns:
        HttpResponse: Renderiza la plantilla 'admin_panel/detalle_principio.html'
                      con el formulario correspondiente.
    """
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
    """
    Elimina un principio dado su ID.

    Solo acepta peticiones POST. Acceso restringido a staff.

    Args:
        _ (HttpRequest): Objeto de la petición HTTP (no se usa).
        principio_id (int): ID del principio a eliminar.

    Returns:
        HttpResponseRedirect: Redirige a la lista de principios tras eliminar el principio.
    """
    principio = Principio.objects.get(pk=principio_id)  # Busca el principio
    if principio:
        principio.delete()  # Elimina de la base de datos
    return redirect('admin_panel:principios')  # Redirige a la lista de principios
