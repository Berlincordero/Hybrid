from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_plantas, name='listar_plantas'),
    path('panel/', views.panel_vivero, name='panel_vivero'),
    path('crear/', views.crear_planta, name='crear_planta'),
    path('crear_mapa/', views.crear_mapa, name='crear_mapa'),
    path('crear_bodega/', views.crear_bodega, name='crear_bodega'),
    path('empleados_subir/', views.crear_empleado, name='crear_empleado'),
    path('crear_gasto/', views.crear_gasto, name='crear_gasto'),
    path('gasto/<int:gasto_id>/editar/', views.editar_gasto, name='editar_gasto'),
    path('mapa/<int:mapa_id>/eliminar/', views.eliminar_mapa, name='eliminar_mapa'),
    path('bodega/<int:bodega_id>/editar/', views.editar_bodega, name='editar_bodega'),
    path('bodega/<int:bodega_id>/eliminar/', views.eliminar_bodega, name='eliminar_bodega'),
    path('empleado/<int:empleado_id>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
    path('empleado/<int:empleado_id>/editar/', views.editar_empleado, name='editar_empleado'),
    path('gasto/<int:gasto_id>/eliminar/', views.eliminar_gasto, name='eliminar_gasto'),
    path('<int:planta_id>/eliminar/', views.eliminar_planta, name='eliminar_planta'),
    path('sembradio/<int:block_num>/', views.listar_sembradio, name='listar_sembradio'),
    path('monitorear/<int:planta_id>/', views.monitorear_planta, name='monitorear_planta'),
]
