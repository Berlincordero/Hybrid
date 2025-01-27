from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketplace_list, name='marketplace_list'),
    path('nuevo/', views.producto_create, name='producto_create'),
    path('<int:pk>/', views.producto_detail, name='producto_detail'),
    path('mis-productos/', views.my_products, name='my_products'),
    path('<int:pk>/edit/', views.producto_edit, name='producto_edit'),
    path('<int:pk>/delete/', views.producto_delete, name='producto_delete'),
]
