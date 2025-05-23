from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpRequest

def redirect_to_login(request: HttpRequest):
    """
    Redirige a la página de login.

    Args:
        request (HttpRequest): Petición HTTP que contiene la sesión del usuario.

    Returns:
        HttpResponseRedirect: Redirección a la ruta 'users/login'.
    """
    if request.user.is_authenticated:
        return redirect('home/')
    else:
        return redirect('users/login')


def sign_out(request: HttpRequest):
    """
    Cierra la sesión del usuario y redirige a la página de login.

    Args:
        request (HttpRequest): Petición HTTP que contiene la sesión del usuario.

    Returns:
        HttpResponseRedirect: Redirección a la ruta 'users/login'.
    """
    logout(request)  # Cierra la sesión
    return redirect('users/login')
