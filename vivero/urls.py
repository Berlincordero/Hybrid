from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_plantas, name='listar_plantas'),
    path('panel/', views.panel_vivero, name='panel_vivero'),
    path('crear/', views.crear_planta, name='crear_planta'),
    path('<int:planta_id>/eliminar/', views.eliminar_planta, name='eliminar_planta'),
    path('sembradio/<int:block_num>/', views.listar_sembradio, name='listar_sembradio'),
    path('monitorear/<int:planta_id>/', views.monitorear_planta, name='monitorear_planta'),
]
