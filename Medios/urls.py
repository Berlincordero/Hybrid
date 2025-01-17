from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos_list, name='videos_list'),
    path('subir/', views.video_upload, name='video_upload'),
]
