# indices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_indices, name='listar_indices'),
    path('lugares-recomendados/', views.listar_lugares_recomendados, name='listar_lugares_recomendados'),
    path('lugares-recomendados/crear/', views.crear_lugar_recomendado, name='crear_lugar_recomendado'),
    path('panama/', views.indice_panama, name='indice_panama'),
    path('nicaragua/', views.indice_nicaragua, name='indice_nicaragua'),
    path('el_salvador/', views.indice_el_salvador, name='indice_el_salvador'),
    path('guatemala/', views.indice_guatemala, name='indice_guatemala'),
    path('mexico/', views.indice_mexico, name='indice_mexico'),
    path('honduras/', views.indice_honduras, name='indice_honduras'),
]

