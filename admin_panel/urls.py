from django.urls import path

from admin_panel.views import dashboard, estrategia_list, principios_list
from admin_panel.views.actualizar_orden import actualizar_orden

app_name = 'admin_panel'
urlpatterns = [
    path('', view=dashboard, name="dashboard"),
    path('estrategias/', view=estrategia_list, name="estrategias"),
    path('principios/', view=principios_list, name="principios"),
    # descriptores

    #actualizar_orden
    path('actualizar_orden/', actualizar_orden, name="actualizar_orden")
]