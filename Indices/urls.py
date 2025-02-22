# indices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_indices, name='listar_indices'),
    path('lugares-recomendados/', views.listar_lugares_recomendados, name='listar_lugares_recomendados'),
    path('lugares-recomendados/crear/', views.crear_lugar_recomendado, name='crear_lugar_recomendado'),
    path('panama/', views.indice_panama, name='indice_panama'),
    path('nicaragua/crear/', views.crear_indice_nicaragua, name='crear_indice_nicaragua'),
    path('nicaragua/', views.indice_nicaragua, name='indice_nicaragua'),
    path('el_salvador/', views.indice_el_salvador, name='indice_el_salvador'),
    path('el_salvador/crear/', views.crear_indice_el_salvador, name='crear_indice_el_salvador'),
    path('guatemala/', views.indice_guatemala, name='indice_guatemala'),
    path('guatemala/crear/', views.crear_indice_guatemala, name='crear_indice_guatemala'),
    path('mexico/', views.indice_mexico, name='indice_mexico'),
    path('mexico/crear/', views.crear_indice_mexico, name='crear_indice_mexico'),
    path('honduras/', views.indice_honduras, name='indice_honduras'),
    path('honduras/crear/', views.crear_indice_honduras, name='crear_indice_honduras'),
    path('crear/', views.crear_indice, name='crear_indice'),
    path('editar/<int:pk>/', views.editar_indice, name='editar_indice'),
    path('panama/', views.indice_panama, name='indice_panama'),
    path('panama/crear/', views.crear_indice_panama, name='crear_indice_panama'),
]

