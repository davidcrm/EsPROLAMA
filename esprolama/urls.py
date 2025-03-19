"""
URL configuration for esprolama project.

The `urlpatterns` list routes URLs to views_delete. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views_delete
    1. Add an import:  from my_app import views_delete
    2. Add a URL to urlpatterns:  path('', views_delete.home, name='home')
Class-based views_delete
    1. Add an import:  from other_app.views_delete import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('elama.urls')),
    path('users/', include('users.urls')),
]
