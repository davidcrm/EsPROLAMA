from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest
from django.shortcuts import render

from elama.models import Descriptor


@staff_member_required
def descriptor_list(request: HttpRequest):
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
    descriptores = Descriptor.objects.all().order_by('step')

    return render(request,'admin_panel/descriptores_list.html',{
        'descriptores':descriptores,
        'links': links,
    })