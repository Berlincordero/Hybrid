# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_fincas, name='listar_fincas'),
    path('crear/', views.crear_finca, name='crear_finca'),
    path('eliminar/<int:finca_id>/', views.eliminar_finca, name='eliminar_finca'),
    path('administrar/<int:finca_id>/', views.administrar_finca, name='administrar_finca'),
    path('editar-imagen/<int:finca_id>/', views.editar_finca_imagen, name='editar_finca_imagen'),
    path('organizar/<int:finca_id>/', views.organizar_finca, name='organizar_finca'),
    
    # Nuevas rutas para división:
    path('editar-division/<int:division_id>/', views.editar_division, name='editar_division'),
    path('eliminar-division/<int:division_id>/', views.eliminar_division, name='eliminar_division'),
    
    
    # Rutas para subir imágenes en el índice (si las necesitas)
    path('upload-producto-imagen/', views.upload_producto_imagen, name='upload_producto_imagen'),
    path('upload-insumo-imagen/', views.upload_insumo_imagen, name='upload_insumo_imagen'),
    path('upload-animales-imagen/', views.upload_animales_imagen, name='upload_animales_imagen'),
    path('organizar-galpon/<int:finca_id>/', views.organizar_galpon, name='organizar_galpon'),
    path('control-animales/<int:finca_id>/', views.control_animales, name='control_animales'),
    path('eliminar-control-animal/<int:control_id>/', views.eliminar_control_animal, name='eliminar_control_animal'),
]

