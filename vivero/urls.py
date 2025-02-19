from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_plantas, name='listar_plantas'),
    path('panel/', views.panel_vivero, name='panel_vivero'),
    path('crear/', views.crear_planta, name='crear_planta'),
    path('crear_mapa/', views.crear_mapa, name='crear_mapa'),
    path('crear_bodega/', views.crear_bodega, name='crear_bodega'),
    path('mapa/<int:mapa_id>/eliminar/', views.eliminar_mapa, name='eliminar_mapa'),
    path('bodega/<int:bodega_id>/eliminar/', views.eliminar_bodega, name='eliminar_bodega'),
    path('<int:planta_id>/eliminar/', views.eliminar_planta, name='eliminar_planta'),
    path('sembradio/<int:block_num>/', views.listar_sembradio, name='listar_sembradio'),
    path('monitorear/<int:planta_id>/', views.monitorear_planta, name='monitorear_planta'),
]
