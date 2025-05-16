from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    """
    Vista principal de la aplicación.

    Requiere que el usuario esté autenticado para acceder.
    Renderiza la plantilla 'elama/home.html'.

    Args:
        request (HttpRequest): Objeto de la petición HTTP.

    Returns:
        HttpResponse: Respuesta con la página principal renderizada.
    """
    # Renderiza la página principal para usuarios autenticados
    return render(request, 'elama/home.html')
