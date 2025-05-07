from django.urls import path

from admin_panel.views import dashboard, estrategia_list, principios_list
from admin_panel.views.actualizar_orden import actualizar_orden
from admin_panel.views.descriptores import descriptor_list, detalle_descriptor, eliminar_descriptor
from admin_panel.views.estrategias import detalle_estrategia, eliminar_estrategia
from admin_panel.views.principios import detalle_principio, eliminar_principio

app_name = 'admin_panel'
urlpatterns = [
    path('', view=dashboard, name="dashboard"),
    #  Listar estrategias
    path('estrategias/', view=estrategia_list, name="estrategias"),
    #  Listar principios
    path('principios/', view=principios_list, name="principios"),
    #  Listar descriptores
    path('descriptores/', view=descriptor_list, name="descriptores"),
    # actualizar_orden
    path('actualizar_orden/', actualizar_orden, name="actualizar_orden"),
    # URLs para estrategias
    path('estrategia/', detalle_estrategia, name="crear_estrategia"),
    path('estrategia/<int:estrategia_id>/', detalle_estrategia, name="editar_estrategia"),
    path('estrategia/<int:estrategia_id>/eliminar/', eliminar_estrategia, name="eliminar_estrategia"),
    # URLs para principios
    path('principio/', detalle_principio, name="crear_principio"),
    path('principio/<int:principio_id>/', detalle_principio, name="editar_principio"),
    path('principio/<int:principio_id>/eliminar/', eliminar_principio,name="eliminar_principio"),
    # URLs para descriptores
    path('descriptor/', detalle_descriptor, name="crear_descriptor"),
    path('descriptor/<int:descriptor_id>/', detalle_descriptor, name="editar_descriptor"),
    path('descriptor/<int:descriptor_id>/eliminar/', eliminar_descriptor, name="eliminar_descriptor"),

]
