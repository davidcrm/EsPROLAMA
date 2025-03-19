from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from elama.models import Autoevaluacion

# Vista para finalizar una autoevaluación, marcándola como finalizada.
@login_required
def finalizar_individual(request, id_autoevaluacion):
    autoevaluacion = Autoevaluacion.objects.get(pk=id_autoevaluacion)
    autoevaluacion.finalizada = True  # Marca la autoevaluación como finalizada.
    autoevaluacion.save()  # Guarda los cambios.
    return redirect('elama:individual', id_autoevaluacion=id_autoevaluacion)  # Redirige a la vista individual.