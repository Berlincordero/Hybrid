# Perfiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import PerfilForm
# Importa tu Profile desde la app Administrador
from Administrador.models import Profile




@login_required
def actualizar_foto_perfil(request):
    if request.method == 'POST' and request.FILES.get('foto_perfil'):
        perfil = Perfil.objects.get(user=request.user)
        perfil.foto_perfil = request.FILES['foto_perfil']
        perfil.save()
        return redirect('perfil')  # Redirige al perfil después de guardar
    return redirect('perfil')





@login_required
def perfil_view(request):
    # Obtenemos o creamos el Perfil (tu modelo "Perfil")
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    # Obtenemos el Profile (tu modelo "Profile" de la app Administrador)
    # (Asumiendo que se crea automáticamente con tu señal post_save)
    profile = request.user.profile

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Ajusta el nombre de tu URL si es distinto
    else:
        form = PerfilForm(instance=perfil)

    # Enviamos AMBOS objetos al template
    return render(
        request, 
        'perfil.html', 
        {
            'form': form,    # El formulario para tu modelo "Perfil"
            'perfil': perfil,      # El objeto "Perfil"
            'profile': profile,    # El objeto "Profile" (app Administrador)
        }
    )

@login_required
def links_empty_view(request):
    # Solo renderiza tu HTML con el Lottie y mensaje
    return render(request, 'links_empty.html')
