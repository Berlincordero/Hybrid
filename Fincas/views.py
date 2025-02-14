from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Finca, Division
from .forms import FincaForm, DivisionForm
from django.forms import modelformset_factory
from .models import Galpon, GalponDivision
from .forms import GalponForm, GalponDivisionForm
from .forms import ControlAnimalForm

@login_required
def listar_fincas(request):
    """Lista todas las fincas del usuario autenticado."""
    fincas = Finca.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'listar_fincas.html', {'fincas': fincas})

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
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    if request.method == 'POST':
        finca.delete()
        return redirect('listar_fincas')
    return render(request, 'confirmar_eliminar_finca.html', {'finca': finca})

@login_required
def administrar_finca(request, finca_id):
    """
    Vista para administrar una finca específica.
    Se obtiene la finca seleccionada y se listan todas las fincas del usuario.
    """
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    fincas = Finca.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'administrar_finca.html', {'finca': finca, 'fincas': fincas})

@login_required
def editar_finca_imagen(request, finca_id):
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    if request.method == 'POST' and request.FILES.get('imagen'):
        finca.imagen = request.FILES['imagen']
        finca.save()
    return redirect('listar_fincas')

# Vistas para subir imágenes en el índice
@login_required
def upload_producto_imagen(request):
    if request.method == 'POST' and request.FILES.get('imagen'):
        # Aquí deberías implementar la lógica para actualizar la imagen del producto
        pass  # Implementa tu lógica aquí.
    return redirect('listar_fincas')

@login_required
def upload_insumo_imagen(request):
    if request.method == 'POST' and request.FILES.get('imagen'):
        # Implementa la lógica para actualizar la imagen del insumo
        pass  # Implementa tu lógica aquí.
    return redirect('listar_fincas')

@login_required
def upload_animales_imagen(request):
    if request.method == 'POST' and request.FILES.get('imagen'):
        # Implementa la lógica para actualizar la imagen de animales
        pass  # Implementa tu lógica aquí.
    return redirect('listar_fincas')

# Nueva vista para organizar la finca (agregar divisiones)
@login_required
def organizar_finca(request, finca_id):
    """
    Permite agregar divisiones a una finca.
    Se verifica que el tamaño ingresado para la división no supere el área disponible,
    la cual se calcula restando la suma de los tamaños de las divisiones existentes al tamaño total de la finca.
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
# Vista para editar una división
@login_required
def editar_division(request, division_id):
    # Aseguramos que la división pertenezca a una finca del usuario
    division = get_object_or_404(Division, id=division_id, finca__usuario=request.user)
    if request.method == 'POST':
        form = DivisionForm(request.POST, request.FILES, instance=division)
        if form.is_valid():
            form.save()
            return redirect('administrar_finca', finca_id=division.finca.id)
    else:
        form = DivisionForm(instance=division)
    return render(request, 'editar_division.html', {'form': form, 'division': division})

# Vista para eliminar una división
@login_required
def eliminar_division(request, division_id):
    # Aseguramos que la división pertenezca a una finca del usuario
    division = get_object_or_404(Division, id=division_id, finca__usuario=request.user)
    if request.method == 'POST':
        finca_id = division.finca.id
        division.delete()
        return redirect('administrar_finca', finca_id=finca_id)
    return render(request, 'confirmar_eliminar_division.html', {'division': division})

@login_required
def organizar_galpon(request, finca_id):
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    GalponDivisionFormSet = modelformset_factory(GalponDivision, form=GalponDivisionForm, extra=1)
    
    if request.method == 'POST':
        galpon_form = GalponForm(request.POST)
        formset = GalponDivisionFormSet(request.POST, queryset=GalponDivision.objects.none())
        
        if galpon_form.is_valid() and formset.is_valid():
            galpon = galpon_form.save(commit=False)
            galpon.finca = finca
            galpon.save()
            total_divisiones = 0
            for form in formset:
                if form.cleaned_data:
                    division = form.save(commit=False)
                    division.galpon = galpon
                    total_divisiones += division.tamano
                    division.save()
            if galpon.tamano < total_divisiones:
                # Manejo de error: la suma de divisiones supera el tamaño global.
                error = "El total de los tamaños de las divisiones supera el tamaño global del galpón."
                return render(request, 'organizar_galpon.html', {'finca': finca, 'galpon_form': galpon_form, 'formset': formset, 'error': error})
            return redirect('administrar_finca', finca_id=finca.id)
    else:
        galpon_form = GalponForm()
        formset = GalponDivisionFormSet(queryset=GalponDivision.objects.none())
    
    return render(request, 'organizar_galpon.html', {'finca': finca, 'galpon_form': galpon_form, 'formset': formset})

# views.py
@login_required
def control_animales(request, finca_id):
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
    control = get_object_or_404(ControlAnimal, id=control_id, finca__usuario=request.user)
    finca_id = control.finca.id
    if request.method == 'POST':
        control.delete()
        return redirect('administrar_finca', finca_id=finca_id)
    # Puedes optar por confirmar la eliminación o redirigir directamente
    return render(request, 'confirmar_eliminar_control_animal.html', {'control': control})