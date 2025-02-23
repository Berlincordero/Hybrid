# indices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Índices - Costa Rica
    path('', views.listar_indices, name='listar_indices'),
    path('crear/', views.crear_indice, name='crear_indice'),
    path('editar/<int:pk>/', views.editar_indice, name='editar_indice'),

    # Lugares Recomendados
    path('lugares-recomendados/', views.listar_lugares_recomendados, name='listar_lugares_recomendados'),
    path('lugares-recomendados/crear/', views.crear_lugar_recomendado, name='crear_lugar_recomendado'),
    # Nueva URL para comentarios en Lugares
    path('lugares-recomendados/<int:lugar_pk>/comentario/', views.add_comentario_lugar, name='add_comentario_lugar'),
    # Nueva URL para reacciones con emojis
    path('lugares-recomendados/<int:lugar_pk>/reaccion/<str:tipo>/', views.reaccionar_lugar, name='reaccionar_lugar'),

    # Índices - Panamá
    path('panama/', views.indice_panama, name='indice_panama'),
    path('panama/crear/', views.crear_indice_panama, name='crear_indice_panama'),

    # Índices - Nicaragua
    path('nicaragua/', views.indice_nicaragua, name='indice_nicaragua'),
    path('nicaragua/crear/', views.crear_indice_nicaragua, name='crear_indice_nicaragua'),

    # Índices - El Salvador
    path('el_salvador/', views.indice_el_salvador, name='indice_el_salvador'),
    path('el_salvador/crear/', views.crear_indice_el_salvador, name='crear_indice_el_salvador'),

    # Índices - Guatemala
    path('guatemala/', views.indice_guatemala, name='indice_guatemala'),
    path('guatemala/crear/', views.crear_indice_guatemala, name='crear_indice_guatemala'),

    # Índices - México
    path('mexico/', views.indice_mexico, name='indice_mexico'),
    path('mexico/crear/', views.crear_indice_mexico, name='crear_indice_mexico'),

    # Índices - Honduras
    path('honduras/', views.indice_honduras, name='indice_honduras'),
    path('honduras/crear/', views.crear_indice_honduras, name='crear_indice_honduras'),
    
     # Nueva URL para ver los negocios del usuario
    path('mis-negocios/', views.mis_negocios, name='mis_negocios'),
    # URLs para editar y eliminar un negocio
    path('mis-negocios/editar/<int:pk>/', views.editar_lugar_recomendado, name='editar_lugar_recomendado'),
    path('mis-negocios/eliminar/<int:pk>/', views.eliminar_lugar_recomendado, name='eliminar_lugar_recomendado'),
]
