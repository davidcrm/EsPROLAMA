from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpRequest

# Vista de login que redirige al usuario a la página de login.
def login(_):
    return redirect('users/login')

def sign_out(request: HttpRequest):
    logout(request)
    return redirect('users/login')
