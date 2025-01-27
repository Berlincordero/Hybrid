from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto, ImagenProducto, VideoProducto
from .forms import ProductoForm

def marketplace_list(request):
    productos = Producto.objects.all()
    context = {
        "productos": productos,
    }
    return render(request, "marketplace_list.html", context)

@login_required
def producto_create(request):
    """
    Crea un nuevo producto y procesa múltiples imágenes y videos.
    """
    if request.method == "POST":
        # Notar que la categoría vendrá en request.POST['categoria'] si usas input hidden
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user
            producto.save()

            # Procesar varias imágenes
            # 'imagenes' es el name del input en el template (con multiple)
            imagenes = request.FILES.getlist('imagenes')
            for img in imagenes:
                ImagenProducto.objects.create(producto=producto, imagen=img)

            # Procesar varios videos
            videos = request.FILES.getlist('videos')
            for vid in videos:
                VideoProducto.objects.create(producto=producto, video=vid)

            messages.success(request, "¡Producto creado con éxito!")
            return redirect("marketplace_list")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = ProductoForm()
    context = {
        "form": form,
    }
    return render(request, "producto_create.html", context)

def producto_detail(request, pk):
    """
    Muestra el detalle de un producto específico.
    """
    producto = get_object_or_404(Producto, pk=pk)
    context = {
        'producto': producto,
    }
    return render(request, 'producto_detail.html', context)

@login_required
def my_products(request):
    """
    Lista los productos del usuario actual.
    """
    productos = Producto.objects.filter(vendedor=request.user)
    return render(request, 'my_products.html', {'productos': productos})

@login_required
def producto_edit(request, pk):
    """
    Edita un producto existente (solo si el usuario logueado es el vendedor).
    """
    producto = get_object_or_404(Producto, pk=pk)
    if producto.vendedor != request.user:
        messages.error(request, "No tienes permiso para editar este producto.")
        return redirect('marketplace_list')

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            # Si sube nuevas imágenes o videos, se agregan a lo existente
            imagenes = request.FILES.getlist('imagenes')
            for img in imagenes:
                ImagenProducto.objects.create(producto=producto, imagen=img)
            videos = request.FILES.getlist('videos')
            for vid in videos:
                VideoProducto.objects.create(producto=producto, video=vid)

            messages.success(request, "¡Producto editado con éxito!")
            return redirect('my_products')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'producto_create.html', {
        'form': form,
        'edit_mode': True,
        'producto': producto
    })

@login_required
def producto_delete(request, pk):
    """
    Elimina un producto si el usuario logueado es el dueño.
    """
    producto = get_object_or_404(Producto, pk=pk)
    if producto.vendedor != request.user:
        messages.error(request, "No tienes permiso para borrar este producto.")
        return redirect('marketplace_list')

    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return redirect('marketplace_list')

    return render(request, 'producto_delete_confirm.html', {'producto': producto})
