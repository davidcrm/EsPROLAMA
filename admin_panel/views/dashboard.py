from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render

@staff_member_required
def dashboard(request: HttpRequest):
    links = [
        {'label': 'Dashboard', 'href': '/admin_panel/'},
        {'label': 'Estrategias', 'href': '/admin_panel/estrategias/'},
        {'label': 'Principios', 'href': '/admin_panel/principios/'},
        {'label': 'Descriptores', 'href': '/admin_panel/descriptores/'},
        {'label': 'Usuarios', 'href': '/admin_panel/usuarios/'},
    ]


    return render(request, 'admin_panel/dashboard.html', {
        'links': links,
        'current_path': request.path
    })