# Perfiles/context_processors.py
from .models import Perfil

def user_profile_context(request):
    """
    Retorna el perfil del usuario logueado (si lo hay), 
    para que esté disponible en todas las plantillas.
    """
    if request.user.is_authenticated:
        perfil = Perfil.objects.filter(user=request.user).first()
        return {'perfil': perfil}
    return {}