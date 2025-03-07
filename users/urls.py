from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # URLs de autenticación predeterminadas de Django.
    path('', include('django.contrib.auth.urls')),
]