from django.urls import path

from .views.auth import login, sign_out
from .views.autoevaluacion import mis_autoevaluaciones
from .views.home import home
from .views.individual import crear_individual, nuevo_individual, individual_descriptor, finalizar_individual

app_name = 'elama'
urlpatterns = [
    # Página de inicio (login).
    path('', login, name="login"),
    # Página de cierre de sesión
    path('logout', sign_out, name="logout"),
    # Página principal con información sobre las autoevaluaciones del usuario (usuario autenticado).
    path('dashboard/', mis_autoevaluaciones, name="dashboard"),
    # Página creación de autoevaluación (individual o grupal)
    path('home/', home, name='home'),
    # Página de creación de nueva autoevaluación individual.
    path('individual/', crear_individual, name='crear-individual'),
    # Página del listado de los descriptores de la autoevaluación individual.
    path('individual/<int:autoevaluacion_id>/', nuevo_individual, name='individual'),
    # Página de valoración de un descriptor.
    path('individual/<int:autoevaluacion_id>/<int:descriptor_id>/', individual_descriptor, name='individual-descriptor'),
    # Página de finalización de autoevaluación individual.
    path('finalizar-individual/<int:id_autoevaluacion>/', finalizar_individual, name='finalizar-individual'),
]
