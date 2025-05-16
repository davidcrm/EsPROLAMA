from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render


@staff_member_required
def dashboard(request: HttpRequest):
    """
    Vista protegida que renderiza el panel de control del administrador.

    Solo accesible para usuarios staff autenticados.

    Muestra una lista de enlaces de navegación para las diferentes secciones
    del panel de administración personalizado.

    Args:
        request (HttpRequest): Objeto HttpRequest de la petición entrante.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'admin_panel/dashboard.html'
        y el contexto con los enlaces de navegación y la ruta actual.
    """
    links = [
        {'label': 'Dashboard', 'href': '/admin_panel/'},
        {'label': 'Usuarios', 'href': '/admin_panel/usuarios/'},
        {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
        {'label': 'Principios', 'href': '/admin_panel/principios/'},
        {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
    ]

    return render(request, 'admin_panel/dashboard.html', {
        'links': links,
        'current_path': request.path
    })
