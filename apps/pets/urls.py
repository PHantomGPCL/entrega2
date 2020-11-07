from django.urls import path
from .views import Inicio

urlpatterns = [
    path('Inicio',Inicio.as_view(), name = 'index')
]
