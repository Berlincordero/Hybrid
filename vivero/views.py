# views.py
import math
from collections import defaultdict, Counter
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localdate
from .models import Planta, Vivero, Monitoreo
from .forms import PlantaForm, ViveroForm, MonitoreoForm, PlantaImagenForm 

def calcular_recomendacion(planta):
    """
    (Se mantiene igual que tu código previo, sin cambios de lógica)
    """
    recommendations = {
        'tomate': {
            'distancia_entre_plantas': (0.6, 0.9),
            'distancia_entre_filas': (1.2, 1.5),
            'area_por_planta': (0.72, 1.35),
            'consumo_agua_recomendado': "5-10 L/por semana por planta",
            'consumo_fertilizante_recomendado': "100-150 g/mes por planta",
            'observaciones': "Depende si es determinado o indeterminado."
        },
        'lechuga': {
            'distancia_entre_plantas': (0.2, 0.3),
            'distancia_entre_filas': (0.3, 0.3),
            'area_por_planta': (0.06, 0.09),
            'consumo_agua_recomendado': "2-4 L/por semana por planta",
            'consumo_fertilizante_recomendado': "50-100 g/mes por planta",
            'observaciones': "Varía según la variedad y manejo."
        },
        'zanahoria': {
            'distancia_entre_plantas': (0.05, 0.08),
            'distancia_entre_filas': (0.25, 0.25),
            'area_por_planta': (0.0125, 0.02),
            'consumo_agua_recomendado': "1-2 L/por semana por planta",
            'consumo_fertilizante_recomendado': "20-40 g/mes por planta",
            'observaciones': "Siembra densa y luego se aclara."
        },
        'ejote': {
            'distancia_entre_plantas': (0.1, 0.15),
            'distancia_entre_filas': (0.5, 0.6),
            'area_por_planta': (0.05, 0.09),
            'consumo_agua_recomendado': "3-5 L/ por semana por planta",
            'consumo_fertilizante_recomendado': "60-90 g/mes por planta",
            'observaciones': "Se cultiva en hilera o con espaldera."
        },
        # Agrega más variedades aquí...
    }

    rec = recommendations.get(planta.variedad)
    if not rec:
        return None

    avg_area_planta = sum(rec['area_por_planta']) / 2.0
    if planta.area_sembrar and planta.area_sembrar > 0:
        area_efectiva = planta.area_sembrar * 0.8
    else:
        area_efectiva = 0

    num_plantas = math.floor(area_efectiva / avg_area_planta) if avg_area_planta > 0 else 0

    prob = 100
    if planta.calidad_suelo == 'baja':
        prob -= 30
    elif planta.calidad_suelo == 'media':
        prob -= 15
    if planta.sistema_riego == 'manual':
        prob -= 10

    return {
        'recomendacion': rec,
        'avg_area_por_planta': avg_area_planta,
        'area_efectiva': area_efectiva,
        'num_plantas_posibles': num_plantas,
        'probabilidad_exito': prob,
    }

@login_required
def panel_vivero(request):
    """
    (Sin cambios)
    """
    vivero, created = Vivero.objects.get_or_create(
        usuario=request.user,
        defaults={'espacio_total': 100}
    )
    plantas = vivero.plantas.all()
    espacio_ocupado = sum(planta.espacio_requerido for planta in plantas)
    espacio_libre = vivero.espacio_total - espacio_ocupado
    consumo_total_agua = sum(planta.consumo_agua for planta in plantas)
    consumo_total_fertilizante = sum(planta.consumo_fertilizante for planta in plantas)

    context = {
        'vivero': vivero,
        'plantas': plantas,
        'espacio_ocupado': espacio_ocupado,
        'espacio_libre': espacio_libre,
        'consumo_total_agua': consumo_total_agua,
        'consumo_total_fertilizante': consumo_total_fertilizante,
    }
    return render(request, 'panel_vivero.html', context)



@login_required
def listar_plantas(request):
    """
    Lista plantas/cultivos, recomendaciones, agrupa por variedad, asigna 'sembradio',
    permite editar el nombre del vivero, registrar monitoreos y ahora también editar la imagen
    desde el mismo template.
    """
    # Vivero
    vivero, _ = Vivero.objects.get_or_create(
        usuario=request.user,
        defaults={'espacio_total': 100}
    )
    
    if request.method == 'POST':
        action = request.POST.get('action')
        # Procesa el formulario de monitoreo
        if action == 'monitoreo':
            plant_id = request.POST.get('plant_id')
            planta = get_object_or_404(Planta, id=plant_id, usuario=request.user)
            monitoreo_form = MonitoreoForm(request.POST)
            if monitoreo_form.is_valid():
                monitoreo = monitoreo_form.save(commit=False)
                monitoreo.planta = planta
                monitoreo.save()
                return redirect('listar_plantas')
        # Procesa la edición de la imagen
        elif action == 'editar_imagen':
            plant_id = request.POST.get('plant_id')
            planta = get_object_or_404(Planta, id=plant_id, usuario=request.user)
            imagen_form = PlantaImagenForm(request.POST, request.FILES, instance=planta)
            if imagen_form.is_valid():
                imagen_form.save()
                return redirect('listar_plantas')
        # Procesa la edición del nombre del vivero
        elif 'vivero_name' in request.POST:
            nuevo_nombre = request.POST.get('vivero_name', '').strip()
            if nuevo_nombre:
                vivero.nombre = nuevo_nombre
                vivero.save()

    plantas = Planta.objects.filter(usuario=request.user).order_by('variedad', 'id')
    recomendaciones = {}
    for p in plantas:
        recomendaciones[p.id] = calcular_recomendacion(p)

    grupos = defaultdict(list)
    for p in plantas:
        grupos[p.variedad].append(p)

    plant_block_info = {}
    for variedad, group in grupos.items():
        group_sorted = sorted(group, key=lambda x: x.id)
        rec = calcular_recomendacion(group_sorted[0])
        capacity = rec["num_plantas_posibles"] if (rec and rec["num_plantas_posibles"] > 0) else 1
        block_numbers = []
        for i, pl in enumerate(group_sorted):
            block_num = (i // capacity) + 1
            block_numbers.append(block_num)

        counts = Counter(block_numbers)
        for i, pl in enumerate(group_sorted):
            block_num = block_numbers[i]
            count_in_block = counts[block_num]
            remaining = capacity - count_in_block
            avg_area = rec["avg_area_por_planta"] if rec else 0
            plant_block_info[pl.id] = {
                'block_num': block_num,
                'capacity': capacity,
                'count_in_block': count_in_block,
                'remaining': remaining,
                'avg_area': avg_area,
            }

    context = {
        'vivero': vivero,
        'plantas': plantas,
        'recomendaciones': recomendaciones,
        'plant_block_info': plant_block_info,
    }
    return render(request, 'listar_plantas.html', context)

@login_required
def crear_planta(request):
    """
    (Sin cambios)
    """
    if request.method == 'POST':
        form = PlantaForm(request.POST, request.FILES)
        if form.is_valid():
            planta = form.save(commit=False)
            planta.usuario = request.user
            vivero, created = Vivero.objects.get_or_create(
                usuario=request.user,
                defaults={'espacio_total': 100}
            )
            planta.vivero = vivero
            planta.save()
            return redirect('listar_plantas')
    else:
        form = PlantaForm()
    return render(request, 'crear_planta.html', {'form': form})

@login_required
def eliminar_planta(request, planta_id):
    """
    Elimina un cultivo.
    """
    planta = get_object_or_404(Planta, id=planta_id, usuario=request.user)
    if request.method == 'POST':
        planta.delete()
        return redirect('listar_plantas')
    return render(request, 'eliminar_planta.html', {'planta': planta})

@login_required
def listar_sembradio(request, block_num):
    """
    (Sin cambios)
    """
    plantas = Planta.objects.filter(usuario=request.user).order_by('variedad', 'id')
    recomendaciones = {}
    for p in plantas:
        recomendaciones[p.id] = calcular_recomendacion(p)

    grupos = defaultdict(list)
    for p in plantas:
        grupos[p.variedad].append(p)

    plant_block_info = {}
    for variedad, group in grupos.items():
        group_sorted = sorted(group, key=lambda x: x.id)
        rec = calcular_recomendacion(group_sorted[0])
        capacity = rec["num_plantas_posibles"] if (rec and rec["num_plantas_posibles"] > 0) else 1
        block_numbers = []
        for i, pl in enumerate(group_sorted):
            block_num_calc = (i // capacity) + 1
            block_numbers.append(block_num_calc)
        counts = Counter(block_numbers)
        for i, pl in enumerate(group_sorted):
            bn = block_numbers[i]
            count_in_block = counts[bn]
            remaining = capacity - count_in_block
            avg_area = rec["avg_area_por_planta"] if rec else 0
            plant_block_info[pl.id] = {
                'block_num': bn,
                'capacity': capacity,
                'count_in_block': count_in_block,
                'remaining': remaining,
                'avg_area': avg_area,
            }
    plantas_filtradas = [p for p in plantas if plant_block_info[p.id]['block_num'] == block_num]

    context = {
        'plantas': plantas_filtradas,
        'recomendaciones': recomendaciones,
        'plant_block_info': plant_block_info,
        'block_num': block_num,
    }
    return render(request, 'listar_sembradio.html', context)

@login_required
def monitorear_planta(request, planta_id):
    """
    Crea una observación (Monitoreo) para la planta en la semana actual.
    """
    planta = get_object_or_404(Planta, id=planta_id, usuario=request.user)
    if request.method == 'POST':
        form = MonitoreoForm(request.POST)
        if form.is_valid():
            monitoreo = form.save(commit=False)
            monitoreo.planta = planta
            monitoreo.save()
            return redirect('listar_plantas')
    else:
        form = MonitoreoForm()

    # Obtenemos todos los registros de monitoreo para esta planta
    observaciones = planta.monitoreos.all().order_by('-fecha')

    return render(request, 'monitorear_planta.html', {
        'form': form,
        'planta': planta,
        'observaciones': observaciones,
    })
