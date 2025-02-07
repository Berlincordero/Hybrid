from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_fincas, name='listar_fincas'),
    path('crear/', views.crear_finca, name='crear_finca'),
    path('eliminar/<int:finca_id>/', views.eliminar_finca, name='eliminar_finca'),

]
