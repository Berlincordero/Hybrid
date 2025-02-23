from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro_list, name="foro_list"),
    path('nuevo/', views.foro_create, name="foro_create"),
    path('comentario/<int:pk>/', views.add_comentario, name="add_comentario"),
    path('repost/<int:pk>/', views.repost_foro, name="repost_foro"),
    path('feed/', views.foro_feed, name="foro_feed"),

    # Reacciones a foros
    path('reaccion/<int:pk>/<str:reaction>/', views.reaccionar_foro, name="reaccionar_foro"),

    # Reacciones a comentarios
    path('reaccion_comentario/<int:comentario_pk>/<str:reaction>/', views.reaccionar_comentario, name="reaccionar_comentario"),
]
