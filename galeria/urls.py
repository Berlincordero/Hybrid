from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_archivos, name='listar_archivos'),
    path('subir/', views.subir_archivo, name='subir_archivo'),
    path('archivo/<int:archivo_id>/', views.detalle_archivo, name='detalle_archivo'),
]
