from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_grupos, name='listar_grupos'),
    path('grupo/<int:grupo_id>/', views.detalle_grupo, name='detalle_grupo'),
    path('crear-grupo/', views.crear_grupo, name='crear_grupo'),
    path('grupo/<int:grupo_id>/crear-publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('publicacion/<int:publicacion_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
]
