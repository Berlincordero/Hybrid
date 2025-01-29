from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketplace_list, name='marketplace_list'),
    
    path('my-products/', views.my_products, name='my_products'),
    
    # Crear producto (para cualquier categoría) -> /create/
    path('create/', views.producto_create, name='producto_create'),
    
    # Detalle de producto: /detail/<category>/<pk>/
    path('detail/<str:category>/<int:pk>/', views.producto_detail, name='producto_detail'),
    
    # Eliminar producto: /delete/<category>/<pk>/
    path('delete/<str:category>/<int:pk>/', views.producto_delete, name='producto_delete'),
    
]
