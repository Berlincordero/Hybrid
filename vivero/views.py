from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Planta, Vivero
from .forms import PlantaForm, ViveroForm

@login_required
def panel_vivero(request):
    vivero, created = Vivero.objects.get_or_create(usuario=request.user)
    plantas = vivero.plantas.all()

    espacio_ocupado = sum(planta.espacio_requerido for planta in plantas)
    espacio_libre = vivero.espacio_total - espacio_ocupado
    consumo_total_agua = sum(planta.consumo_agua for planta in plantas)
    consumo_total_fertilizante = sum(planta.consumo_fertilizante for planta in plantas)

    return render(request, 'panel_vivero.html', {
        'vivero': vivero,
        'plantas': plantas,
        'espacio_ocupado': espacio_ocupado,
        'espacio_libre': espacio_libre,
        'consumo_total_agua': consumo_total_agua,
        'consumo_total_fertilizante': consumo_total_fertilizante,
    })

@login_required
def listar_plantas(request):
    plantas = Planta.objects.filter(usuario=request.user).order_by('-fecha_adquisicion')
    return render(request, 'listar_plantas.html', {'plantas': plantas})

@login_required
def crear_planta(request):
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
    planta = get_object_or_404(Planta, id=planta_id, usuario=request.user)
    if request.method == 'POST':
        planta.delete()
        return redirect('listar_plantas')
    return render(request, 'eliminar_planta.html', {'planta': planta})