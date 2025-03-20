from django.urls import path
from .views.crear_indiviudal import crear_individual
from .views.dashboard import dashboard
from .views.finalizar_individual import finalizar_individual
from .views.individual import individual
from .views.login import login
from .views.main import main
from .views.volcar_autoevaluacion import volcar_autoevaluacion

app_name = 'elama'
urlpatterns = [
    # Página de inicio (login).
    path('', login, name="login"),
    # Página principal con información sobre las autoevaluaciones del usuario (usuario autenticado).
    path('dashboard/', dashboard, name="dashboard"),
    # Página creación de autoevaluación (individual o grupal)
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