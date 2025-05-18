from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from admin_panel.forms.estrategia_form import EstrategiaForm
from elama.models import Estrategia

links = [
    {'label': 'Dashboard', 'href': '/admin_panel/'},
    {'label': 'Usuarios', 'href': '/admin_panel/usuarios/'},
    {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
    {'label': 'Principios', 'href': '/admin_panel/principios/'},
    {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
]


@staff_member_required
def estrategia_list(request: HttpRequest):
    """
    Vista protegida que muestra la lista de estrategias ordenadas por su campo `step`.

    Solo accesible a usuarios con permisos de staff.

    Args:
        request (HttpRequest): Objeto HttpRequest de la petición entrante.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'admin_panel/estrategia_list.html'
        mostrando la lista de estrategias y los enlaces de navegación.
    """
    estrategias = Estrategia.objects.all().order_by('step')

    return render(request, 'admin_panel/estrategia_list.html', {
        'estrategias': estrategias,
        'links': links,
    })


@staff_member_required
def detalle_estrategia(request: HttpRequest, estrategia_id: int = None):
    """
    Vista protegida para crear o editar una estrategia.

    Si se recibe un estrategia_id, se edita la estrategia correspondiente.
    Si no, se crea una nueva.

    Solo accesible a usuarios con permisos de staff.

    Args:
        request (HttpRequest): Objeto HttpRequest de la petición entrante.
        estrategia_id (int, optional): ID de la estrategia a editar. Por defecto None (crear).

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'admin_panel/detalle_estrategia.html'
        mostrando el formulario de edición o creación.
    """
    estrategia = Estrategia.objects.get(pk=estrategia_id) if estrategia_id else None

    if request.method == 'POST':
        form = EstrategiaForm(request.POST, instance=estrategia)

        if form.is_valid():
            form.save()
            if not estrategia_id:
                return redirect('admin_panel:estrategias')
            messages.success(request, '¡Estrategia actualizada con éxito!')

    else:
        form = EstrategiaForm(instance=estrategia)

    return render(request, 'admin_panel/detalle_estrategia.html', {
        'estrategia': estrategia,
        'form': form,
        'links': links
    })


@staff_member_required
@require_POST
def eliminar_estrategia(_, estrategia_id: int):
    """
    Vista protegida para eliminar una estrategia.

    Solo acepta peticiones POST y requiere permisos de staff.

    Args:
        _ (HttpRequest): Objeto HttpRequest (no se usa).
        estrategia_id (int): ID de la estrategia a eliminar.

    Returns:
        HttpResponseRedirect: Redirige a la lista de estrategias tras eliminar.
    """
    estrategia = Estrategia.objects.get(pk=estrategia_id)
    if estrategia:
        estrategia.delete()
    return redirect('admin_panel:estrategias')
