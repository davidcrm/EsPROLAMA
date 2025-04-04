from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Vista principal, solo accesible para usuarios autenticados.
@login_required
def home(request):
    return render(request, 'elama/home.html')