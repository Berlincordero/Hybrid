# views.py (Fincas)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.db.models import Count

# IMPORTA Indice
from Indices.models import Indice

from .models import Finca, Division, Galpon, GalponDivision, ControlAnimal, PersonalFinca, GastoFinca
from .forms import FincaForm, DivisionForm, GalponForm, GalponDivisionForm, ControlAnimalForm, PersonalFincaForm, GastoFincaForm
import json

@login_required
def listar_fincas(request):
    """Lista todas las fincas del usuario autenticado y además trae los vegetales del índice."""
    fincas = Finca.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    
    # Consulta de índices de la subcategoría "vegetales"
    vegetales = Indice.objects.filter(sub_categoria='vegetales').order_by('-fecha')

    return render(request, 'listar_fincas.html', {
        'fincas': fincas,
        'vegetales': vegetales,  # Pasamos esta queryset al template
    })


@login_required
def crear_finca(request):
    """Crea una nueva finca."""
    if request.method == 'POST':
        form = FincaForm(request.POST, request.FILES)
        if form.is_valid():
            finca = form.save(commit=False)
            finca.usuario = request.user
            finca.save()
            return redirect('listar_fincas')
    else:
        form = FincaForm()
    return render(request, 'crear_finca.html', {'form': form})

@login_required
def eliminar_finca(request, finca_id):
    """Elimina una finca, previa confirmación."""
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    if request.method == 'POST':
        finca.delete()
        return redirect('listar_fincas')
    return render(request, 'confirmar_eliminar_finca.html', {'finca': finca})


@login_required
def crear_personal_finca(request, finca_id):
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    if request.method == 'POST':
        form = PersonalFincaForm(request.POST, request.FILES)
        if form.is_valid():
            personal = form.save(commit=False)
            personal.finca = finca
            personal.save()
            return redirect('administrar_finca', finca_id=finca.id)
    else:
        form = PersonalFincaForm()
    return render(request, 'crear_personal_finca.html', {'form': form, 'finca': finca})

@login_required
def editar_personal_finca(request, personal_id):
    personal = get_object_or_404(PersonalFinca, id=personal_id, finca__usuario=request.user)
    if request.method == 'POST':
        form = PersonalFincaForm(request.POST, request.FILES, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('administrar_finca', finca_id=personal.finca.id)
    else:
        form = PersonalFincaForm(instance=personal)
    return render(request, 'editar_personal_finca.html', {'form': form, 'personal': personal})

@login_required
def eliminar_personal_finca(request, personal_id):
    personal = get_object_or_404(PersonalFinca, id=personal_id, finca__usuario=request.user)
    finca_id = personal.finca.id
    if request.method == 'POST':
        personal.delete()
        return redirect('administrar_finca', finca_id=finca_id)
    return render(request, 'confirmar_eliminar_personal_finca.html', {'personal': personal})

@login_required
def administrar_finca(request, finca_id):
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    fincas = Finca.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    
    total_animales_galpon = sum(
        gd.animales for gd in GalponDivision.objects.filter(galpon__finca=finca)
    )
    
    control_animales = finca.control_animales.all()
    if control_animales.exists():
        avg_weight = sum(ca.peso for ca in control_animales) / control_animales.count()
    else:
        avg_weight = None
    rendimiento_promedio = f"{avg_weight:.2f}" if avg_weight is not None else "N/A"
    
    composition = finca.control_animales.values('tipo_animal').annotate(count=Count('id'))
    labels = [entry['tipo_animal'] for entry in composition]
    values = [entry['count'] for entry in composition]
    composition_labels = json.dumps(labels)
    composition_values = json.dumps(values)
    
    galpon_division_data = {}
    for galpon in finca.galpones.all():
        divisions = galpon.divisiones.all()
        labels_div = [f"División {i+1}" for i, div in enumerate(divisions)]
        data_div = [div.tamaño for div in divisions]
        galpon_division_data[galpon.id] = {
            "labels": labels_div,
            "data": data_div,
            "nombre": galpon.nombre,
            "total": galpon.tamano,
        }
    galpon_division_data_json = json.dumps(galpon_division_data)
    
    personal_list = finca.personal.all()
    gastos_list = finca.gastos.all()
    
    context = {
        'finca': finca,
        'fincas': fincas,
        'total_animales_galpon': total_animales_galpon,
        'rendimiento_promedio': rendimiento_promedio,
        'composition_labels': composition_labels,
        'composition_values': composition_values,
        'galpon_division_data_json': galpon_division_data_json,
        'personal_list': personal_list,
        'gastos_list': gastos_list,
    }
    return render(request, 'administrar_finca.html', context)
@login_required
def editar_finca_imagen(request, finca_id):
    """Permite actualizar únicamente la imagen de una finca."""
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    if request.method == 'POST' and request.FILES.get('imagen'):
        finca.imagen = request.FILES['imagen']
        finca.save()
    return redirect('listar_fincas')

@login_required
def upload_producto_imagen(request):
    """(Ejemplo) Manejo de imagen para un producto."""
    if request.method == 'POST' and request.FILES.get('imagen'):
        pass
    return redirect('listar_fincas')

@login_required
def upload_insumo_imagen(request):
    """(Ejemplo) Manejo de imagen para un insumo."""
    if request.method == 'POST' and request.FILES.get('imagen'):
        pass
    return redirect('listar_fincas')

@login_required
def upload_animales_imagen(request):
    """(Ejemplo) Manejo de imagen para un animal."""
    if request.method == 'POST' and request.FILES.get('imagen'):
        pass
    return redirect('listar_fincas')

@login_required
def organizar_finca(request, finca_id):
    """
    Permite agregar divisiones a una finca.
    Verifica que el tamaño ingresado para la división no supere el área disponible
    (tamaño total de la finca - divisiones ya existentes).
    """
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    used_area = sum(division.tamaño for division in finca.divisiones.all())
    remaining_area = finca.tamaño - used_area

    if request.method == 'POST':
        form = DivisionForm(request.POST, request.FILES)
        if form.is_valid():
            division = form.save(commit=False)
            division.finca = finca
            if division.tamaño > remaining_area:
                form.add_error('tamaño', f"El tamaño de la división supera el área restante ({remaining_area} m²).")
            else:
                division.save()
                return redirect('administrar_finca', finca_id=finca.id)
    else:
        form = DivisionForm()

    return render(request, 'organizar_finca.html', {
        'form': form,
        'finca': finca,
        'remaining_area': remaining_area,
    })

@login_required
def editar_division(request, division_id):
    """Edita los datos de una división concreta."""
    division = get_object_or_404(Division, id=division_id, finca__usuario=request.user)
    if request.method == 'POST':
        form = DivisionForm(request.POST, request.FILES, instance=division)
        if form.is_valid():
            form.save()
            return redirect('administrar_finca', finca_id=division.finca.id)
    else:
        form = DivisionForm(instance=division)
    return render(request, 'editar_division.html', {'form': form, 'division': division})

@login_required
def eliminar_division(request, division_id):
    """Elimina una división de la finca, previa confirmación."""
    division = get_object_or_404(Division, id=division_id, finca__usuario=request.user)
    if request.method == 'POST':
        finca_id = division.finca.id
        division.delete()
        return redirect('administrar_finca', finca_id=finca_id)
    return render(request, 'confirmar_eliminar_division.html', {'division': division})

@login_required
def organizar_galpon(request, finca_id):
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    GalponDivisionFormSet = modelformset_factory(
        GalponDivision,
        form=GalponDivisionForm,
        extra=1
    )
    
    if request.method == 'POST':
        # Se añade request.FILES
        galpon_form = GalponForm(request.POST, request.FILES)
        formset = GalponDivisionFormSet(request.POST, queryset=GalponDivision.objects.none())
        
        if galpon_form.is_valid() and formset.is_valid():
            galpon = galpon_form.save(commit=False)
            galpon.finca = finca
            galpon.save()
            
            total_divisiones = 0
            for f in formset:
                if f.cleaned_data:
                    division = f.save(commit=False)
                    division.galpon = galpon
                    division.save()
                    total_divisiones += division.tamano
            if total_divisiones > galpon.tamano:
                galpon.delete()
                error = "El total de los tamaños de las divisiones supera el tamaño global del galpón."
                return render(
                    request,
                    'organizar_galpon.html',
                    {
                        'finca': finca,
                        'galpon_form': galpon_form,
                        'formset': formset,
                        'error': error
                    }
                )
            return redirect('administrar_finca', finca_id=finca.id)
    else:
        galpon_form = GalponForm()
        formset = GalponDivisionFormSet(queryset=GalponDivision.objects.none())
    
    return render(request, 'organizar_galpon.html', {
        'finca': finca,
        'galpon_form': galpon_form,
        'formset': formset
    })


@login_required
def control_animales(request, finca_id):
    """Control de animales: crea nuevos registros y lista los existentes."""
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    control_animales = finca.control_animales.all().order_by('-fecha_control')
    
    if request.method == 'POST':
        form = ControlAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            control = form.save(commit=False)
            control.finca = finca
            control.save()
            return redirect('administrar_finca', finca_id=finca.id)
    else:
        form = ControlAnimalForm()
    
    return render(request, 'control_animales.html', {
        'finca': finca,
        'control_animales': control_animales,
        'form': form,
    })

@login_required
def eliminar_control_animal(request, control_id):
    """Elimina un registro de ControlAnimal, previa confirmación."""
    control = get_object_or_404(ControlAnimal, id=control_id, finca__usuario=request.user)
    finca_id = control.finca.id
    if request.method == 'POST':
        control.delete()
        return redirect('administrar_finca', finca_id=finca_id)
    return render(request, 'confirmar_eliminar_control_animal.html', {'control': control})

# ---------------------------------------------------
# NUEVAS VISTAS PARA EDITAR Y ELIMINAR GALPÓN
# ---------------------------------------------------
@login_required
def editar_galpon(request, galpon_id):
    galpon = get_object_or_404(Galpon, id=galpon_id, finca__usuario=request.user)
    if request.method == 'POST':
        # Añadir request.FILES
        form = GalponForm(request.POST, request.FILES, instance=galpon)
        if form.is_valid():
            form.save()
            return redirect('administrar_finca', finca_id=galpon.finca.id)
    else:
        form = GalponForm(instance=galpon)
    return render(request, 'editar_galpon.html', {'form': form, 'galpon': galpon})

@login_required
def eliminar_galpon(request, galpon_id):
    """Elimina un galpón, previa confirmación."""
    galpon = get_object_or_404(Galpon, id=galpon_id, finca__usuario=request.user)
    finca_id = galpon.finca.id
    if request.method == 'POST':
        galpon.delete()
        return redirect('administrar_finca', finca_id=finca_id)
    return render(request, 'confirmar_eliminar_galpon.html', {'galpon': galpon})



@login_required
def administrar_costos_ficas(request, finca_id):
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    if request.method == 'POST':
        form = GastoFincaForm(request.POST, request.FILES)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.finca = finca
            gasto.save()
            return redirect('administrar_finca', finca_id=finca.id)
    else:
        form = GastoFincaForm()
    return render(request, 'administrar_costos_fincas.html', {'form': form, 'finca': finca})

@login_required
def editar_gasto_finca(request, gasto_id):
    gasto = get_object_or_404(GastoFinca, id=gasto_id, finca__usuario=request.user)
    if request.method == 'POST':
        form = GastoFincaForm(request.POST, request.FILES, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('administrar_finca', finca_id=gasto.finca.id)
    else:
        form = GastoFincaForm(instance=gasto)
    return render(request, 'editar_costos_fincas.html', {'form': form, 'gasto': gasto})

@login_required
def eliminar_gasto_finca(request, gasto_id):
    gasto = get_object_or_404(GastoFinca, id=gasto_id, finca__usuario=request.user)
    finca_id = gasto.finca.id
    if request.method == 'POST':
        gasto.delete()
        return redirect('administrar_finca', finca_id=finca_id)
    return render(request, 'confirmar_eliminar_gasto_finca.html', {'gasto': gasto})