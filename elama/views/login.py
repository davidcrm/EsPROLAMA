from django.shortcuts import redirect

# Vista de login que redirige al usuario a la página de login.
def login(request):
    return redirect('users/login')
