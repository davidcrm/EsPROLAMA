from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from admin_panel.forms.estrategia_form import EstrategiaForm
from elama.models import Estrategia

# Vista para listar todas las estrategias disponibles
@staff_member_required
def estrategia_list(request: HttpRequest):
    # Enlaces de navegación del panel de administración
    links = [
        {'label': 'Dashboard', 'href': '/admin_panel/'},
        {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
        {'label': 'Principios', 'href': '/admin_panel/principios/'},
        {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
    ]
    # Consulta todas las estrategias ordenadas por 'step'
    estrategias = Estrategia.objects.all().order_by('step')

    # Renderiza la plantilla con la lista de estrategias y enlaces
    return render(request, 'admin_panel/estrategia_list.html', {
        'estrategias': estrategias,
        'links': links,
    })


# Vista para crear o editar una estrategia
@staff_member_required
def detalle_estrategia(request: HttpRequest, estrategia_id: int = None):
    # Enlaces de navegación del panel de administración
    links = [
        {'label': 'Dashboard', 'href': '/admin_panel/'},
        {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
        {'label': 'Principios', 'href': '/admin_panel/principios/'},
        {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
    ]

    estrategia = None
    # Si se recibe un ID, busca la estrategia a editar
    if estrategia_id:
        estrategia = Estrategia.objects.get(pk=estrategia_id)

    # Si el formulario se envía (POST)
    if request.method == 'POST':
        form = EstrategiaForm(request.POST, instance=estrategia)  # Crea o actualiza
        if form.is_valid():
            form.save()  # Guarda los cambios o crea nueva estrategia
            return redirect('admin_panel:estrategias')  # Redirige a la lista
    else:
        form = EstrategiaForm(instance=estrategia)  # Formulario vacío o con datos

    # Renderiza la plantilla de detalle (crear o editar) con el formulario y enlaces
    return render(request, 'admin_panel/detalle_estrategia.html', {
        'estrategia': estrategia,
        'form': form,
        'links': links
    })


# Vista para eliminar una estrategia (solo acepta POST)
@staff_member_required
@require_POST
def eliminar_estrategia(request: HttpRequest, estrategia_id: int):
    estrategia = Estrategia.objects.get(pk=estrategia_id)  # Busca la estrategia
    estrategia.delete()  # Elimina de la base de datos
    return redirect('admin_panel:estrategias')  # Redirige a la lista de estrategias
