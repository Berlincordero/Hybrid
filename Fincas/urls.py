# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_fincas, name='listar_fincas'),
    path('crear/', views.crear_finca, name='crear_finca'),
    path('eliminar/<int:finca_id>/', views.eliminar_finca, name='eliminar_finca'),
    path('administrar/<int:finca_id>/', views.administrar_finca, name='administrar_finca'),
    path('editar-imagen/<int:finca_id>/', views.editar_finca_imagen, name='editar_finca_imagen'),
    
    # Nuevas rutas para subir imágenes en el índice:
    path('upload-producto-imagen/', views.upload_producto_imagen, name='upload_producto_imagen'),
    path('upload-insumo-imagen/', views.upload_insumo_imagen, name='upload_insumo_imagen'),
    path('upload-animales-imagen/', views.upload_animales_imagen, name='upload_animales_imagen'),
]
