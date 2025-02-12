# indices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_indices, name='listar_indices'),
    path('lugares-recomendados/', views.listar_lugares_recomendados, name='listar_lugares_recomendados'),
    path('lugares-recomendados/crear/', views.crear_lugar_recomendado, name='crear_lugar_recomendado'),
]
