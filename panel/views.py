from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Configuracion
from .forms import ConfiguracionForm

@login_required
def ver_configuracion(request):
    """Vista para ver la configuración actual."""
    configuracion, created = Configuracion.objects.get_or_create(usuario=request.user)
    return render(request, 'ver_configuracion.html', {'configuracion': configuracion})

@login_required
def actualizar_configuracion(request):
    """Vista para actualizar la configuración."""
    configuracion, created = Configuracion.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST, instance=configuracion)
        if form.is_valid():
            form.save()
            return redirect('ver_configuracion')
    else:
        form = ConfiguracionForm(instance=configuracion)
    return render(request, 'actualizar_configuracion.html', {'form': form})
