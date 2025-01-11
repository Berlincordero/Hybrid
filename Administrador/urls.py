# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  
    path('login/', views.login_view, name='login_view'),  
    path('logout/', views.logout_view, name='logout'),
    path('mas-informacion/', views.mas_informacion, name='mas_informacion'),
    path('condiciones-uso/', views.condiciones_uso, name='condiciones_uso'),
    path('politica-privacidad/', views.politica_privacidad, name='politica_privacidad'),
    path('politica-cookies/', views.politica_cookies, name='politica_cookies'),
    path('contacto/', views.enviar_contacto, name='enviar_contacto'),
    path('lockout/', views.lockout, name='lockout'),
    path('', views.index, name='index'),  # Ruta para la página principal
]
