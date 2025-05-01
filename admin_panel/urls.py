from django.urls import path

from .views import dashboard

app_name = 'admin_panel'
urlpatterns = [
    path('', view=dashboard, name="dashboard"),
]