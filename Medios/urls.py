from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos_list, name='videos_list'),
    path('subir/', views.video_upload, name='video_upload'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('video/<int:pk>/like/', views.video_like, name='video_like'),
    # Nueva URL para la galería personal
    path('mis-videos/', views.personal_gallery, name='personal_gallery'),
]
