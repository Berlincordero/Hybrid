from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Planta
from .forms import PlantaForm

@login_required
def listar_plantas(request):
    """Lista todas las plantas del usuario autenticado."""
    plantas = Planta.objects.filter(usuario=request.user).order_by('-fecha_adquisicion')
    return render(request, 'listar_plantas.html', {'plantas': plantas})

@login_required
def crear_planta(request):
    """Crea una nueva planta."""
    if request.method == 'POST':
        form = PlantaForm(request.POST, request.FILES)
        if form.is_valid():
            planta = form.save(commit=False)
            planta.usuario = request.user
            planta.save()
            return redirect('listar_plantas')
    else:
        form = PlantaForm()
    return render(request, 'crear_planta.html', {'form': form})

@login_required
def eliminar_planta(request, planta_id):
    """Elimina una planta existente."""
    planta = get_object_or_404(Planta, id=planta_id, usuario=request.user)
    if request.method == 'POST':
        planta.delete()
        return redirect('listar_plantas')
    return render(request, 'eliminar_planta.html', {'planta': planta})
