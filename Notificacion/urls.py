from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notificaciones, name='listar_notificaciones'),
    path('<int:notificacion_id>/marcar-leido/', views.marcar_leido, name='marcar_leido'),
]
