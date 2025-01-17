from django.urls import path
from . import views

urlpatterns = [
    path('', views.opiniones, name='opiniones'),
]