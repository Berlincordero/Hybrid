from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_fincas, name='listar_fincas'),
    path('crear/', views.crear_finca, name='crear_finca'),
    path('eliminar/<int:finca_id>/', views.eliminar_finca, name='eliminar_finca'),
    path('administrar/<int:finca_id>/', views.administrar_finca, name='administrar_finca'),
    path('editar-imagen/<int:finca_id>/', views.editar_finca_imagen, name='editar_finca_imagen'),
    path('organizar/<int:finca_id>/', views.organizar_finca, name='organizar_finca'),
    path('editar-division/<int:division_id>/', views.editar_division, name='editar_division'),
    path('eliminar-division/<int:division_id>/', views.eliminar_division, name='eliminar_division'),
    path('upload-producto-imagen/', views.upload_producto_imagen, name='upload_producto_imagen'),
    path('upload-insumo-imagen/', views.upload_insumo_imagen, name='upload_insumo_imagen'),
    path('upload-animales-imagen/', views.upload_animales_imagen, name='upload_animales_imagen'),
    path('organizar-galpon/<int:finca_id>/', views.organizar_galpon, name='organizar_galpon'),
    path('control-animales/<int:finca_id>/', views.control_animales, name='control_animales'),
    path('eliminar-control-animal/<int:control_id>/', views.eliminar_control_animal, name='eliminar_control_animal'),
    path('galpon/editar/<int:galpon_id>/', views.editar_galpon, name='editar_galpon'),
    path('galpon/eliminar/<int:galpon_id>/', views.eliminar_galpon, name='eliminar_galpon'),
    path('crear-personal/<int:finca_id>/', views.crear_personal_finca, name='crear_personal_finca'),
    path('editar-personal/<int:personal_id>/', views.editar_personal_finca, name='editar_personal_finca'),
    path('eliminar-personal/<int:personal_id>/', views.eliminar_personal_finca, name='eliminar_personal_finca'),
    path('administrar_costos_fincas/<int:finca_id>/', views.administrar_costos_ficas, name='administrar_costos_fincas'),
    path('editar-gasto/<int:gasto_id>/', views.editar_gasto_finca, name='editar_gasto_finca'),
    path('eliminar-gasto/<int:gasto_id>/', views.eliminar_gasto_finca, name='eliminar_gasto_finca'),
]
