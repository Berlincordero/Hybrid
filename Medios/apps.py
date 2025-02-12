from django.apps import AppConfig


class MediosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Medios'


class VideosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Opcional, pero recomendable en Django 3.2+
    name = 'videos'  # Asegúrate de que este nombre coincida con el de tu carpeta de la app "videos"

    def ready(self):
        # Importa el módulo signals para que se conecten los receivers al iniciar la app.
        import Medios.signals
