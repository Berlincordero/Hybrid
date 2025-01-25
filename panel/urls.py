from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_configuracion, name='ver_configuracion'),
    path('actualizar/', views.actualizar_configuracion, name='actualizar_configuracion'),
]
