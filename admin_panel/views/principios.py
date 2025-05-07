from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from admin_panel.forms.principio_form import PrincipioForm
from elama.models import Principio


@staff_member_required
def principios_list(request: HttpRequest):
    links = [
        {'label': 'Dashboard', 'href': '/admin_panel/'},
        {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
        {'label': 'Principios', 'href': '/admin_panel/principios/'},
        {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
    ]
    principios = Principio.objects.all().order_by('step')

    return render(request,'admin_panel/principios_list.html',{
        'principios':principios,
        'links': links,
    })

@staff_member_required
def detalle_principio(request: HttpRequest, principio_id: int = None):
    # Enlaces de navegación del panel de administración
    links = [
        {'label': 'Dashboard', 'href': '/admin_panel/'},
        {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
        {'label': 'Principios', 'href': '/admin_panel/principios/'},
        {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
    ]

    principio = None
    # Si se recibe un ID, busca el principio a editar
    if principio_id:
        principio = Principio.objects.get(pk=principio_id)

    # Si el formulario se envía (POST)
    if request.method == 'POST':
        form = PrincipioForm(request.POST, instance=principio)  # Crea o actualiza
        if form.is_valid():
            form.save()  # Guarda los cambios o crea nueva principio
            return redirect('admin_panel:principios')  # Redirige a la lista
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
def eliminar_principio(request: HttpRequest, principio_id: int):
    principio = Principio.objects.get(pk=principio_id)  # Busca el principio
    principio.delete()  # Elimina de la base de datos
    return redirect('admin_panel:principios')  # Redirige a la lista de principios