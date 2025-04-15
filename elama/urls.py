from django.urls import path

from .views.auth import login, sign_out
from .views.home import home
from .views.grupal import grupal
from .views.individual import individual, detalle_individual, individual_descriptor, finalizar_individual

app_name = 'elama'
urlpatterns = [
    # Página de inicio (login).
    path('', login, name="login"),
    # Página de cierre de sesión
    path('logout', sign_out, name="logout"),
    # Página creación de autoevaluación (individual o grupal)
    path('home/', home, name='home'),
    # Página de creación de nueva autoevaluación individual.
    path('individual/', individual, name='individual'),
    # Página del listado de los descriptores de la autoevaluación individual.
    path('individual/<int:autoevaluacion_id>/', detalle_individual, name='individual-detail'),
    # Página de valoración de un descriptor.
    path('individual/<int:autoevaluacion_id>/<int:descriptor_id>/', individual_descriptor, name='individual-descriptor'),
    # Página de finalización de autoevaluación individual.
    path('finalizar-individual/<int:autoevaluacion_id>/', finalizar_individual, name='finalizar-individual'),
    # Página para elegir usuarios pertenecientes a una evaluación grupal
    path('grupal/', grupal, name='grupal'),

]
