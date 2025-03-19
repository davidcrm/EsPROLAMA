# Vista para crear una nueva autoevaluación, solo accesible para usuarios autenticados.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from elama.models import Autoevaluacion


@login_required
def crear_individual(request):
    autoevaluacion = Autoevaluacion()  # Crea una nueva instancia de Autoevaluacion.
    autoevaluacion.save()  # Guarda la autoevaluación en la base de datos.
    return redirect('elama:individual', id_autoevaluacion=autoevaluacion.id)  # Redirige a la vista individual.