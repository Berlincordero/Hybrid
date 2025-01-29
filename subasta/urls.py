# subasta/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_subastas, name='listar_subastas'),
    path('crear/', views.crear_subasta, name='crear_subasta'),
]
