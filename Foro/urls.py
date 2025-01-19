from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro_list, name="foro_list"),
    path('nuevo/', views.foro_create, name="foro_create"),
    path('comentario/<int:pk>/', views.add_comentario, name="add_comentario"),
    path('estrella/<int:pk>/', views.toggle_estrella, name="toggle_estrella"),
    path('repost/<int:pk>/', views.repost_foro, name="repost_foro"),
]
