

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render

from elama.models import Estrategia

@staff_member_required
def estrategia_list(request: HttpRequest):
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
    estrategias = Estrategia.objects.all().order_by('step')

    return render(request,'admin_panel/estrategia_list.html',{
        'estrategias':estrategias,
        'links': links,
    })

