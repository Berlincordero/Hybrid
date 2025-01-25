from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_plantas, name='listar_plantas'),
    path('crear/', views.crear_planta, name='crear_planta'),
    path('<int:planta_id>/eliminar/', views.eliminar_planta, name='eliminar_planta'),
]
