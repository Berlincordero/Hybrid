# config/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views
import Administrador.views as Administrador_views
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Habilita la vista set_language
]

# Envolver las URLs principales con i18n_patterns para manejar el idioma en las URLs
urlpatterns += i18n_patterns(
    path('', Administrador_views.login_view, name='login_view'),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('Administrador/', include('Administrador.urls')),
    path('Perfiles/', include('Perfiles.urls')),
    path('Friends/', include('Friends.urls')), # <--- Aquí importamos nuestras URLs de 'friends'
    path('chats/', include('chats.urls')),
    path('opiniones/', include('opiniones.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)