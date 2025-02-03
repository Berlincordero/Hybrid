import math
from collections import defaultdict, Counter
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Planta, Vivero
from .forms import PlantaForm, ViveroForm

def calcular_recomendacion(planta):
    """
    Calcula las recomendaciones de espaciamiento, área efectiva,
    número de plantas posibles y probabilidad de éxito basado en los
    parámetros del cultivo (variedad, calidad del suelo, sistema de riego, etc.).
    """
    recommendations = {
        'tomate': {
            'distancia_entre_plantas': (0.6, 0.9),
            'distancia_entre_filas': (1.2, 1.5),
            'area_por_planta': (0.72, 1.35),
            'consumo_agua_recomendado': "5-10 L/semana",
            'consumo_fertilizante_recomendado': "100-150 g/mes",
            'observaciones': "Depende si es determinado o indeterminado."
        },
        'lechuga': {
            'distancia_entre_plantas': (0.2, 0.3),
            'distancia_entre_filas': (0.3, 0.3),
            'area_por_planta': (0.06, 0.09),
            'consumo_agua_recomendado': "2-4 L/semana",
            'consumo_fertilizante_recomendado': "50-100 g/mes",
            'observaciones': "Varía según la variedad y manejo."
        },
        'zanahoria': {
            'distancia_entre_plantas': (0.05, 0.08),
            'distancia_entre_filas': (0.25, 0.25),
            'area_por_planta': (0.0125, 0.02),
            'consumo_agua_recomendado': "1-2 L/semana",
            'consumo_fertilizante_recomendado': "20-40 g/mes",
            'observaciones': "Siembra densa y luego se aclara."
        },
        'ejote': {
            'distancia_entre_plantas': (0.1, 0.15),
            'distancia_entre_filas': (0.5, 0.6),
            'area_por_planta': (0.05, 0.09),
            'consumo_agua_recomendado': "3-5 L/semana",
            'consumo_fertilizante_recomendado': "60-90 g/mes",
            'observaciones': "Se cultiva en hilera o con espaldera."
        },
        # Puedes agregar más variedades aquí...
    }

    rec = recommendations.get(planta.variedad)
    if not rec:
        return None

    # Calculamos el promedio del área requerida por planta
    avg_area_planta = sum(rec['area_por_planta']) / 2.0

    # Se descuenta un 20% del área asignada para caminos, manejo y riego
    if planta.area_sembrar and planta.area_sembrar > 0:
        area_efectiva = planta.area_sembrar * 0.8
    else:
        area_efectiva = 0

    # Calculamos cuántas plantas caben en el área efectiva
    num_plantas = math.floor(area_efectiva / avg_area_planta) if avg_area_planta > 0 else 0

    # Se asigna una probabilidad de éxito básica
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
    Muestra el panel del vivero con datos generales: espacio ocupado, libre,
    y consumos totales de agua y fertilizante.
    """
    vivero, created = Vivero.objects.get_or_create(
        usuario=request.user,
        defaults={'espacio_total': 100}  # Valor por defecto, ajusta según sea necesario
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
    Lista todas las plantas/cultivos registrados por el usuario, calcula las recomendaciones
    y agrupa (por variedad) asignando un "número de sembradio" de forma secuencial según la
    capacidad (número de plantas posibles) recomendada.

    Además, permite editar el nombre del Vivero en la misma página.
    """
    # Se obtiene o crea el Vivero asociado al usuario
    vivero, _ = Vivero.objects.get_or_create(
        usuario=request.user,
        defaults={'espacio_total': 100}
    )

    # Si se envía un POST con 'vivero_name', actualizamos el nombre sin redirigir
    if request.method == 'POST' and 'vivero_name' in request.POST:
        nuevo_nombre = request.POST.get('vivero_name', '').strip()
        if nuevo_nombre:
            vivero.nombre = nuevo_nombre
            vivero.save()

    # Obtenemos las plantas ordenadas por variedad e id
    plantas = Planta.objects.filter(usuario=request.user).order_by('variedad', 'id')
    
    # Calculamos la recomendación para cada planta
    recomendaciones = {}
    for planta in plantas:
        recomendaciones[planta.id] = calcular_recomendacion(planta)
    
    # Agrupamos por variedad
    grupos = defaultdict(list)
    for planta in plantas:
        grupos[planta.variedad].append(planta)
    
    # Asignamos un número de "sembradio" secuencial según la capacidad
    plant_block_info = {}
    for variedad, group in grupos.items():
        group_sorted = sorted(group, key=lambda x: x.id)
        rec = calcular_recomendacion(group_sorted[0])
        capacity = rec["num_plantas_posibles"] if (rec and rec["num_plantas_posibles"] > 0) else 1
        block_numbers = []
        for i, planta in enumerate(group_sorted):
            block_num = (i // capacity) + 1
            block_numbers.append(block_num)
        counts = Counter(block_numbers)
        for i, planta in enumerate(group_sorted):
            block_num = block_numbers[i]
            count_in_block = counts[block_num]
            remaining = capacity - count_in_block
            avg_area = rec["avg_area_por_planta"] if rec else 0
            plant_block_info[planta.id] = {
                'block_num': block_num,
                'capacity': capacity,
                'count_in_block': count_in_block,
                'remaining': remaining,
                'avg_area': avg_area,
            }
    
    context = {
        'plantas': plantas,
        'recomendaciones': recomendaciones,
        'plant_block_info': plant_block_info,
        'vivero': vivero,
    }
    return render(request, 'listar_plantas.html', context)

@login_required
def crear_planta(request):
    if request.method == 'POST':
        form = PlantaForm(request.POST, request.FILES)
        if form.is_valid():
            planta = form.save(commit=False)
            planta.usuario = request.user
            # Obtener o crear el vivero con un valor por defecto para 'espacio_total'
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
    Elimina un cultivo/plantación del vivero.
    """
    planta = get_object_or_404(Planta, id=planta_id, usuario=request.user)
    if request.method == 'POST':
        planta.delete()
        return redirect('listar_plantas')
    return render(request, 'eliminar_planta.html', {'planta': planta})
