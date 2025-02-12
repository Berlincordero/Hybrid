# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video
from .utils import optimize_video

@receiver(post_save, sender=Video)
def optimize_video_signal(sender, instance, created, **kwargs):
    """
    Signal que se ejecuta cada vez que se crea un nuevo objeto Video.
    Optimiza el archivo de video usando la función optimize_video.
    """
    if created:
        try:
            optimize_video(instance)
        except Exception as e:
            # Aquí podrías registrar el error en un log o manejarlo de otra forma.
            print(f"Error al optimizar el video: {e}")
