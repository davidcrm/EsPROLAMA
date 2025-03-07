from django.urls import path
from . import views

app_name = 'elama'
urlpatterns = [
    # Página de inicio (login).
    path('', views.login, name="login"),
    # Página principal (usuario autenticado).
    path('main/', views.main, name='main'),
    # Página de creación de nueva autoevaluación individual.
    path('crear-individual/', views.crear_individual, name='crear-individual'),
    # Página de autoevaluación individual.
    path('individual/<int:id_autoevaluacion>/', views.individual, name='individual'),
    # Página de valoración de un descriptor.
    path('individual/<int:id_autoevaluacion>/<int:id_descriptor>/', views.volcar_autoevaluacion, name='volcar-autoevaluacion'),
    # Página de finalización de autoevaluación individual.
    path('finalizar-individual/<int:id_autoevaluacion>/', views.finalizar_individual, name='finalizar-individual'),
]