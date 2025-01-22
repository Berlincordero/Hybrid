from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Perfiles.models import Perfil  # Ajusta la importación según corresponda

@login_required
def index(request):
    # Si el usuario está autenticado, intentamos obtener (o crear) el Perfil
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    
    # Ahora puedes usar 'perfil' en el contexto sin riesgo de error.
    context = {
        'perfil': perfil,
        # Otras variables que necesites
    }
    return render(request, 'index.html', context)
