from django.urls import path
from . import views
from .views import perfil_view, actualizar_foto_perfil

urlpatterns = [
    path('perfil/', views.perfil_view, name='perfil'),  # Página del perfil del usuario
    path('actualizar-foto/', actualizar_foto_perfil, name='actualizar_foto_perfil'),
]