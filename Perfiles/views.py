# Perfiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import PerfilForm

@login_required
def perfil_view(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    
    return render(request, 'perfil.html', {'form': form, 'perfil': perfil})

@login_required
def actualizar_foto_perfil(request):
    if request.method == 'POST' and request.FILES.get('foto_perfil'):
        perfil = Perfil.objects.get(user=request.user)
        perfil.foto_perfil = request.FILES['foto_perfil']
        perfil.save()
        return redirect('perfil')  # Redirige al perfil después de guardar
    return redirect('perfil')