from django.urls import path
from elama.views.crear_indiviudal import crear_individual
from elama.views.finalizar_individual import finalizar_individual
from elama.views.individual import individual
from elama.views.login import login
from elama.views.main import main
from elama.views.volcar_autoevaluacion import volcar_autoevaluacion

app_name = 'elama'
urlpatterns = [
    # Página de inicio (login).
    path('', login, name="login"),
    # Página principal (usuario autenticado).
    path('main/', main, name='main'),
    # Página de creación de nueva autoevaluación individual.
    path('crear-individual/', crear_individual, name='crear-individual'),
    # Página de autoevaluación individual.
    path('individual/<int:id_autoevaluacion>/', individual, name='individual'),
    # Página de valoración de un descriptor.
    path('individual/<int:id_autoevaluacion>/<int:id_descriptor>/', volcar_autoevaluacion, name='volcar-autoevaluacion'),
    # Página de finalización de autoevaluación individual.
    path('finalizar-individual/<int:id_autoevaluacion>/', finalizar_individual, name='finalizar-individual'),
]