from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render

from elama.models import Principio


@staff_member_required
def principios_list(request: HttpRequest):
    links = [
        {
            'label': 'Dashboard',
            'href': '/admin_panel/'
        },
        {
            'label': 'Estrategias',
            'href': '/admin_panel/estrategias/'
        },
        {
            'label': 'Principios',
            'href': '/admin_panel/principios/'
        },
        {
            'label': 'Descriptores',
            'href': '/admin_panel/descriptores/'
        },
    ]
    principios = Principio.objects.all()

    return render(request,'admin_panel/principios_list.html',{
        'principios':principios,
        'links': links,
    })