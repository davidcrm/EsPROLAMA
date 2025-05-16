from bisect import insort

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST

from admin_panel.forms.usuario_form import UsuarioForm

links = [
    {'label': 'Dashboard', 'href': '/admin_panel/'},
    {'label': 'Usuarios', 'href': '/admin_panel/usuarios/'},
    {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
    {'label': 'Principios', 'href': '/admin_panel/principios/'},
    {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
]


@staff_member_required
def usuario_list(request: HttpRequest):
    """
    Obtiene y muestra la lista de usuarios que no son superusuarios ni staff,
    excluyendo al usuario que hace la petición.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.

    Returns:
        HttpResponse: Renderiza la plantilla 'admin_panel/usuario_list.html' con los usuarios y enlaces.
    """
    usuarios = (User.objects
                .filter(is_superuser=False, is_staff=False)
                .exclude(id=request.user.id)
                )

    return render(request, 'admin_panel/usuario_list.html', {
        'usuarios': usuarios,
        'links': links
    })


@staff_member_required
def detalle_usuario(request: HttpRequest, usuario_id: int = None):
    """
    Vista para crear o editar un usuario.

    Si se proporciona un usuario_id, edita el usuario correspondiente.
    Si no, crea uno nuevo.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.
        usuario_id (int, opcional): ID del usuario a editar. Por defecto None.

    Returns:
        HttpResponse: Renderiza la plantilla 'admin_panel/detalle_usuario.html' con el formulario correspondiente.
    """
    usuario = None
    if usuario_id:
        usuario = User.objects.get(pk=usuario_id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:usuarios')
        messages.success(request, '¡Usuario guardado correctamente!')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'admin_panel/detalle_usuario.html', {
        'usuario': usuario,
        'form': form,
        'links': links
    })


@staff_member_required
@require_POST
def eliminar_usuario(_, usuario_id: int):
    """
    Elimina un usuario dado su ID.

    Solo acepta peticiones POST. Acceso restringido a staff.

    Args:
        _ (HttpRequest): Objeto de la petición HTTP (no se usa).
        usuario_id (int): ID del usuario a eliminar.

    Returns:
        HttpResponseRedirect: Redirige a la lista de usuarios tras eliminar el usuario.
    """
    usuario = User.objects.get(pk=usuario_id)  # Busca el usuario
    if usuario:
        usuario.delete()  # Elimina de la base de datos
    return redirect('admin_panel:usuarios')  # Redirige a la lista de usuarios
