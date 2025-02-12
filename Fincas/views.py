from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Finca
from .forms import FincaForm

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
    Muestra la página de administración con el nombre de la finca.
    """
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    return render(request, 'administrar_finca.html', {'finca': finca})

@login_required
def editar_finca_imagen(request, finca_id):
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    if request.method == 'POST' and request.FILES.get('imagen'):
        finca.imagen = request.FILES['imagen']
        finca.save()
        # Opcional: puedes agregar un mensaje de éxito
        # messages.success(request, "Imagen actualizada correctamente.")
    return redirect('listar_fincas')

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
        # Por ejemplo, si tienes un modelo Producto, obtén la instancia correspondiente y actualízala.
        # En este ejemplo, simplemente redirigimos a la lista.
        pass  # Implementa tu lógica aquí
    return redirect('listar_fincas')

@login_required
def upload_insumo_imagen(request):
    if request.method == 'POST' and request.FILES.get('imagen'):
        # Implementa la lógica para actualizar la imagen del insumo
        pass  # Implementa tu lógica aquí
    return redirect('listar_fincas')

@login_required
def upload_animales_imagen(request):
    if request.method == 'POST' and request.FILES.get('imagen'):
        # Implementa la lógica para actualizar la imagen de animales
        pass  # Implementa tu lógica aquí
    return redirect('listar_fincas')