# Perfiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import PerfilForm
from Administrador.models import Profile  # Asegúrate de que la importación sea correcta

@login_required
def actualizar_foto_perfil(request):
    if request.method == 'POST' and request.FILES.get('foto_perfil'):
        # Usamos get_or_create para asegurar que existe el objeto Perfil
        perfil, created = Perfil.objects.get_or_create(user=request.user)
        perfil.foto_perfil = request.FILES['foto_perfil']
        perfil.save()
        return redirect('perfil')  # Redirige a la vista de perfil después de guardar
    return redirect('perfil')


@login_required
def perfil_view(request):
    # Obtenemos o creamos el objeto del modelo "Perfil"
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    # Obtenemos o creamos el objeto "Profile" de la app Administrador
    profile, created_profile = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Asegúrate de que el nombre de la URL sea el correcto
    else:
        form = PerfilForm(instance=perfil)

    # Pasamos ambos objetos al template
    context = {
        'form': form,       # Formulario para el modelo "Perfil"
        'perfil': perfil,   # Objeto "Perfil"
        'profile': profile, # Objeto "Profile" (de la app Administrador)
    }
    return render(request, 'perfil.html', context)


@login_required
def links_empty_view(request):
    # Renderiza el HTML correspondiente sin lógica adicional
    return render(request, 'links_empty.html')
