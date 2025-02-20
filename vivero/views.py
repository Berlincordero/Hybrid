# views.py
import math
from Indices.models import Indice
from collections import defaultdict, Counter
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localdate
from .models import Planta, Vivero, Monitoreo, Mapa, Bodega, Empleado
from .forms import PlantaForm, ViveroForm, MonitoreoForm, PlantaImagenForm, MapaForm, BodegaForm, EmpleadoForm


def calcular_recomendacion(planta):
    """
    Mantiene tus datos de distancias, consumo, observaciones, etc.
    Ajustamos 'area_por_planta' en cada variedad a valores reales,
    de modo que en 1 m² no aparezcan cifras exageradas (ej. 300+).
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
            'distancia_entre_plantas': (0.1, 0.15),
            'distancia_entre_filas': (0.25, 0.3),
            # Ajustado para no tener valores irreales.
            'area_por_planta': (0.20, 0.35),
            'consumo_agua_recomendado': "1-2 L/por semana por planta",
            'consumo_fertilizante_recomendado': "20-40 g/mes por planta",
            'observaciones': "Ajustado para no meter 300+ plantas en 1 m²."
        },
        'ejote': {
            'distancia_entre_plantas': (0.1, 0.15),
            'distancia_entre_filas': (0.5, 0.6),
            'area_por_planta': (0.10, 0.15),
            'consumo_agua_recomendado': "3-5 L/ semana por planta",
            'consumo_fertilizante_recomendado': "60-90 g/mes por planta",
            'observaciones': "Se cultiva en hilera o con espaldera."
        },
        # ... agrega más si necesitas ...
    }

    rec = recommendations.get(planta.variedad)
    if not rec:
        return None  # Si la variedad no está en el dict, retornamos None

    # Calculamos el promedio del rango 'area_por_planta'
    avg_area_planta = sum(rec['area_por_planta']) / 2.0

    # Factor de eficiencia. Ajusta según necesidad: 0.8, 0.5, etc.
    if planta.area_sembrar and planta.area_sembrar > 0:
        area_efectiva = planta.area_sembrar * 0.8
    else:
        area_efectiva = 0

    num_plantas = math.floor(area_efectiva / avg_area_planta) if avg_area_planta > 0 else 0

    prob = 100
    # Opcional: si tienes calidad_suelo, sistema_riego en tu modelo, lo aplicas aquí
    # if planta.calidad_suelo == 'baja':
    #     prob -= 30
    # elif planta.calidad_suelo == 'media':
    #     prob -= 15
    # if planta.sistema_riego == 'manual':
    #     prob -= 10

    return {
        'recomendacion': {
            'distancia_entre_plantas': rec['distancia_entre_plantas'],
            'distancia_entre_filas': rec['distancia_entre_filas'],
            'area_por_planta': rec['area_por_planta'],
            'consumo_agua_recomendado': rec['consumo_agua_recomendado'],
            'consumo_fertilizante_recomendado': rec['consumo_fertilizante_recomendado'],
            'observaciones': rec['observaciones'],
        },
        'avg_area_planta': avg_area_planta,
        'area_efectiva': area_efectiva,
        'num_plantas_posibles': num_plantas,
        'probabilidad_exito': prob,
    }

@login_required
def panel_vivero(request):
    """
    (Tal como tu código previo)
    """
    vivero, _ = Vivero.objects.get_or_create(
        usuario=request.user,
        defaults={'espacio_total': 1}  # Ajusta el default si quieres
    )
    plantas = vivero.plantas.all()
    espacio_ocupado = 0  # O lo que quieras, si no manejas algo extra
    # ...
    context = {
        'vivero': vivero,
        'plantas': plantas,
        # etc...
    }
    return render(request, 'panel_vivero.html', context)

def calcular_recomendacion(planta):
    # Aquí iría tu lógica para recomendaciones
    pass

@login_required
def listar_plantas(request):
    vivero, _ = Vivero.objects.get_or_create(
        usuario=request.user, 
        defaults={'espacio_total': 1}
    )
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'monitoreo':
            pid = request.POST.get('plant_id')
            pl = get_object_or_404(Planta, id=pid, usuario=request.user)
            fm = MonitoreoForm(request.POST)
            if fm.is_valid():
                obj = fm.save(commit=False)
                obj.planta = pl
                obj.save()
                return redirect('listar_plantas')
        elif action == 'editar_imagen':
            pid = request.POST.get('plant_id')
            pl = get_object_or_404(Planta, id=pid, usuario=request.user)
            fi = PlantaImagenForm(request.POST, request.FILES, instance=pl)
            if fi.is_valid():
                fi.save()
                return redirect('listar_plantas')
        elif 'vivero_name' in request.POST:
            nuevo_nombre = request.POST.get('vivero_name', '').strip()
            if nuevo_nombre:
                vivero.nombre = nuevo_nombre
                vivero.save()

    # Todas las plantas del usuario
    plantas = Planta.objects.filter(usuario=request.user).order_by('id')
    # Se obtienen también los mapas creados por el usuario
    mapas = Mapa.objects.filter(usuario=request.user).order_by('id')

    # (Lógica para bloques, recomendaciones, etc.)
    orchard_capacity = vivero.espacio_total
    orchard_area_left = orchard_capacity
    current_block = 1
    count_in_block = 0

    plant_block_info = {}
    recomendaciones = {}

    for p in plantas:
        rec = calcular_recomendacion(p)
        avg_area = rec['avg_area_planta'] if rec else 1.0

        if avg_area > orchard_area_left:
            current_block += 1
            orchard_area_left = orchard_capacity
            count_in_block = 0

        orchard_area_left -= avg_area
        count_in_block += 1

        if avg_area > 0:
            remaining_plants = math.floor(orchard_area_left / avg_area)
        else:
            remaining_plants = 0

        plant_block_info[p.id] = {
            'block_num': current_block,
            'capacity': max(1, math.floor(orchard_capacity / avg_area)),
            'count_in_block': count_in_block,
            'remaining': max(0, remaining_plants),
            'avg_area': avg_area,
        }
        recomendaciones[p.id] = rec

    indices_unificados = Indice.objects.filter(
        sub_categoria__in=['vegetales', 'granos']
    ).order_by('nombre')

    context = {
        'vivero': vivero,
        'plantas': plantas,
        'mapas': mapas,  # Se agrega la lista de mapas
        'plant_block_info': plant_block_info,
        'recomendaciones': recomendaciones,
        'indices': indices_unificados,
    }
    return render(request, 'listar_plantas.html', context)


@login_required
def crear_planta(request):
    """
    Añadir una nueva planta: 
    ya NO existe 'espacio_requerido' en el formulario ni en el modelo,
    solo 'area_sembrar'.
    """
    if request.method == 'POST':
        form = PlantaForm(request.POST, request.FILES)
        if form.is_valid():
            pl = form.save(commit=False)
            pl.usuario = request.user
            viv, _ = Vivero.objects.get_or_create(
                usuario=request.user,
                defaults={'espacio_total': 1}
            )
            pl.vivero = viv
            pl.save()
            return redirect('listar_plantas')
    else:
        form = PlantaForm()
    return render(request, 'crear_planta.html', {'form': form})

@login_required
def eliminar_planta(request, planta_id):
    pl = get_object_or_404(Planta, id=planta_id, usuario=request.user)
    if request.method == 'POST':
        pl.delete()
        return redirect('listar_plantas')
    return render(request, 'eliminar_planta.html', {'planta': pl})

@login_required
def listar_sembradio(request, block_num):
    """
    Repetimos la misma asignación global y luego filtramos
    las plantas que quedaron en ese bloque (block_num).
    """
    vivero, _ = Vivero.objects.get_or_create(
        usuario=request.user, 
        defaults={'espacio_total': 1}
    )
    plantas = Planta.objects.filter(usuario=request.user).order_by('id')

    orchard_capacity = vivero.espacio_total
    orchard_area_left = orchard_capacity
    current_block = 1
    count_in_block = 0

    plant_block_info = {}
    recomendaciones = {}

    for p in plantas:
        rec = calcular_recomendacion(p)
        if rec:
            avg_area = rec['avg_area_planta']
        else:
            avg_area = 1.0

        if avg_area > orchard_area_left:
            current_block += 1
            orchard_area_left = orchard_capacity
            count_in_block = 0

        orchard_area_left -= avg_area
        count_in_block += 1

        if avg_area > 0:
            remaining_plants = math.floor(orchard_area_left / avg_area)
        else:
            remaining_plants = 0

        plant_block_info[p.id] = {
            'block_num': current_block,
            'capacity': max(1, math.floor(orchard_capacity / avg_area)),
            'count_in_block': count_in_block,
            'remaining': max(0, remaining_plants),
            'avg_area': avg_area,
        }
        recomendaciones[p.id] = rec

    # Filtramos las plantas que se ubicaron en 'block_num'
    plantas_filtradas = [x for x in plantas if plant_block_info[x.id]['block_num'] == block_num]

    context = {
        'plantas': plantas_filtradas,
        'plant_block_info': plant_block_info,
        'recomendaciones': recomendaciones,
        'block_num': block_num,
    }
    return render(request, 'listar_sembradio.html', context)

@login_required
def monitorear_planta(request, planta_id):
    pl = get_object_or_404(Planta, id=planta_id, usuario=request.user)
    if request.method == 'POST':
        fm = MonitoreoForm(request.POST)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.planta = pl
            obj.save()
            return redirect('listar_plantas')
    else:
        fm = MonitoreoForm()
    observaciones = pl.monitoreos.all().order_by('-fecha')
    return render(request, 'monitorear_planta.html', {
        'form': fm,
        'planta': pl,
        'observaciones': observaciones,
    })


@login_required
def crear_mapa(request):
    if request.method == 'POST':
        form = MapaForm(request.POST, request.FILES)
        if form.is_valid():
            mapa = form.save(commit=False)
            mapa.usuario = request.user
            mapa.save()
            return redirect('listar_plantas')
    else:
        form = MapaForm()
    return render(request, 'crear_mapa.html', {'form': form})

@login_required
def eliminar_mapa(request, mapa_id):
    mapa = get_object_or_404(Mapa, id=mapa_id, usuario=request.user)
    if request.method == 'POST':
        mapa.delete()
        return redirect('listar_plantas')
    return render(request, 'eliminar_mapa.html', {'mapa': mapa})

@login_required
def crear_bodega(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST, request.FILES)
        if form.is_valid():
            bodega = form.save(commit=False)
            bodega.usuario = request.user
            bodega.save()
            return redirect('listar_plantas')
    else:
        form = BodegaForm()
    return render(request, 'crear_bodega.html', {'form': form})

@login_required
def eliminar_bodega(request, bodega_id):
    bodega = get_object_or_404(Bodega, id=bodega_id, usuario=request.user)
    if request.method == 'POST':
        bodega.delete()
        return redirect('listar_plantas')
    return render(request, 'eliminar_bodega.html', {'bodega': bodega})

@login_required
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.usuario = request.user
            empleado.save()
            return redirect('listar_plantas')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados_subir.html', {'form': form})

@login_required
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id, usuario=request.user)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_plantas')
    return render(request, 'eliminar_empleado.html', {'empleado': empleado})
