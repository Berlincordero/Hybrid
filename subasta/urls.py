# subasta/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_subastas, name='listar_subastas'),
    path('crear/', views.crear_subasta, name='crear_subasta'),
    path('mis-subastas/', views.mis_subastas, name='mis_subastas'),
    path('editar/<int:subasta_id>/', views.editar_subasta, name='editar_subasta'),
    path('eliminar/<int:subasta_id>/', views.eliminar_subasta, name='eliminar_subasta'),
    path('rate/<int:subasta_id>/', views.rate_subasta, name='rate_subasta'),
]
