# indices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_indices, name='listar_indices'),
]
