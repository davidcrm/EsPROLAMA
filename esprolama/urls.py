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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('ZRQqb4xnhTMSfGXcyVooEtR8gWxzPKMc/', admin.site.urls),
    path('admin_panel/', include('admin_panel.urls')),
    path('', include('elama.urls')),
    path('users/', include('users.urls')),
    # estas vistas no dependen de una app concreta. Son genéricas del sistema de autenticación de Django por eso van aqui
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
