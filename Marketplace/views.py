# marketplace/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    FrutasVerduras,
    Animales,
    Ganado,
    Propiedades,
    Vehiculos,
    Insumos,
)

from .forms import (
    FrutasVerdurasForm,
    AnimalesForm,
    GanadoForm,
    PropiedadesForm,
    VehiculosForm,
    InsumosForm,
)

def marketplace_list(request):
    """
    Muestra un listado de todos los productos de todas las categorías.
    """
    frutas_verduras = FrutasVerduras.objects.filter(vendido=False)
    animales = Animales.objects.filter(vendido=False)
    ganado = Ganado.objects.filter(vendido=False)
    propiedades = Propiedades.objects.filter(vendido=False)
    vehiculos = Vehiculos.objects.filter(vendido=False)
    insumos = Insumos.objects.filter(vendido=False)
    
    context = {
        "frutas_verduras": frutas_verduras,
        "animales": animales,
        "ganado": ganado,
        "propiedades": propiedades,
        "vehiculos": vehiculos,
        "insumos": insumos,
    }
    return render(request, "marketplace_list.html", context)

@login_required
def producto_create(request):
    """
    Crea un nuevo producto según la categoría seleccionada.
    """
    if request.method == "POST":
        categoria = request.POST.get("categoria")
        
        if categoria == "frutas_verduras":
            form = FrutasVerdurasForm(request.POST, request.FILES)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.vendedor = request.user
                producto.save()
                messages.success(request, "¡Producto creado con éxito!")
                return redirect("marketplace_list")
        elif categoria == "animales":
            form = AnimalesForm(request.POST, request.FILES)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.vendedor = request.user
                producto.save()
                messages.success(request, "¡Producto creado con éxito!")
                return redirect("marketplace_list")
        elif categoria == "ganado":
            form = GanadoForm(request.POST, request.FILES)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.vendedor = request.user
                producto.save()
                messages.success(request, "¡Producto creado con éxito!")
                return redirect("marketplace_list")
        elif categoria == "propiedades":
            form = PropiedadesForm(request.POST, request.FILES)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.vendedor = request.user
                producto.save()
                messages.success(request, "¡Producto creado con éxito!")
                return redirect("marketplace_list")
        elif categoria == "vehiculos":
            form = VehiculosForm(request.POST, request.FILES)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.vendedor = request.user
                producto.save()
                messages.success(request, "¡Producto creado con éxito!")
                return redirect("marketplace_list")
        elif categoria == "insumos":
            form = InsumosForm(request.POST, request.FILES)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.vendedor = request.user
                producto.save()
                messages.success(request, "¡Producto creado con éxito!")
                return redirect("marketplace_list")
        else:
            messages.error(request, "Categoría no válida o no reconocida.")
            return redirect("marketplace_list")
        
        # Si el formulario no es válido
        messages.error(request, "Por favor corrige los errores del formulario.")
    
    else:
        # GET request, mostrar formularios vacíos
        frutas_form = FrutasVerdurasForm()
        animales_form = AnimalesForm()
        ganado_form = GanadoForm()
        propiedades_form = PropiedadesForm()
        vehiculos_form = VehiculosForm()
        insumos_form = InsumosForm()
        
        context = {
            "frutas_form": frutas_form,
            "animales_form": animales_form,
            "ganado_form": ganado_form,
            "propiedades_form": propiedades_form,
            "vehiculos_form": vehiculos_form,
            "insumos_form": insumos_form,
        }
        return render(request, "producto_create.html", context)
    
    # Si el formulario es inválido, renderiza de nuevo con formularios vacíos o conserva los datos
    frutas_form = FrutasVerdurasForm()
    animales_form = AnimalesForm()
    ganado_form = GanadoForm()
    propiedades_form = PropiedadesForm()
    vehiculos_form = VehiculosForm()
    insumos_form = InsumosForm()
        
    context = {
        "frutas_form": frutas_form,
        "animales_form": animales_form,
        "ganado_form": ganado_form,
        "propiedades_form": propiedades_form,
        "vehiculos_form": vehiculos_form,
        "insumos_form": insumos_form,
    }
    return render(request, "producto_create.html", context)

@login_required
def my_products(request):
    """
    Lista los productos del usuario actual.
    """
    frutas_verduras = FrutasVerduras.objects.filter(vendedor=request.user)
    animales = Animales.objects.filter(vendedor=request.user)
    ganado = Ganado.objects.filter(vendedor=request.user)
    propiedades = Propiedades.objects.filter(vendedor=request.user)
    vehiculos = Vehiculos.objects.filter(vendedor=request.user)
    insumos = Insumos.objects.filter(vendedor=request.user)
    
    context = {
        "frutas_verduras": frutas_verduras,
        "animales": animales,
        "ganado": ganado,
        "propiedades": propiedades,
        "vehiculos": vehiculos,
        "insumos": insumos,
    }
    return render(request, "my_products.html", context)

def producto_detail(request, category, pk):
    """
    Muestra el detalle de un producto específico.
    """
    model = None
    if category == "frutas_verduras":
        model = FrutasVerduras
    elif category == "animales":
        model = Animales
    elif category == "ganado":
        model = Ganado
    elif category == "propiedades":
        model = Propiedades
    elif category == "vehiculos":
        model = Vehiculos
    elif category == "insumos":
        model = Insumos
    else:
        messages.error(request, "Categoría no válida.")
        return redirect("marketplace_list")
    
    producto = get_object_or_404(model, pk=pk)
    context = {
        "producto": producto,
        "category": category,
    }
    return render(request, "producto_detail.html", context)

@login_required
def producto_edit(request, category, pk):
    """
    Edita un producto existente.
    """
    model = None
    form_class = None
    if category == "frutas_verduras":
        model = FrutasVerduras
        form_class = FrutasVerdurasForm
    elif category == "animales":
        model = Animales
        form_class = AnimalesForm
    elif category == "ganado":
        model = Ganado
        form_class = GanadoForm
    elif category == "propiedades":
        model = Propiedades
        form_class = PropiedadesForm
    elif category == "vehiculos":
        model = Vehiculos
        form_class = VehiculosForm
    elif category == "insumos":
        model = Insumos
        form_class = InsumosForm
    else:
        messages.error(request, "Categoría no válida.")
        return redirect("marketplace_list")
    
    producto = get_object_or_404(model, pk=pk)
    if producto.vendedor != request.user:
        messages.error(request, "No tienes permiso para editar este producto.")
        return redirect("marketplace_list")
    
    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Producto editado con éxito!")
            return redirect("my_products")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = form_class(instance=producto)
    
    context = {
        "form": form,
        "producto": producto,
        "category": category,
        "edit_mode": True,
    }
    return render(request, "producto_create.html", context)

@login_required
def producto_delete(request, category, pk):
    """
    Elimina un producto.
    """
    model = None
    if category == "frutas_verduras":
        model = FrutasVerduras
    elif category == "animales":
        model = Animales
    elif category == "ganado":
        model = Ganado
    elif category == "propiedades":
        model = Propiedades
    elif category == "vehiculos":
        model = Vehiculos
    elif category == "insumos":
        model = Insumos
    else:
        messages.error(request, "Categoría no válida.")
        return redirect("marketplace_list")
    
    producto = get_object_or_404(model, pk=pk)
    if producto.vendedor != request.user:
        messages.error(request, "No tienes permiso para borrar este producto.")
        return redirect("marketplace_list")
    
    if request.method == "POST":
        producto.delete()
        messages.success(request, "¡Producto eliminado con éxito!")
        return redirect("marketplace_list")
    
    context = {
        "producto": producto,
        "category": category,
    }
    return render(request, "producto_delete_confirm.html", context)

@login_required
def marcar_vendido(request, category, pk):
    """
    Marca un producto como vendido.
    """
    model = None
    if category == "frutas_verduras":
        model = FrutasVerduras
    elif category == "animales":
        model = Animales
    elif category == "ganado":
        model = Ganado
    elif category == "propiedades":
        model = Propiedades
    elif category == "vehiculos":
        model = Vehiculos
    elif category == "insumos":
        model = Insumos
    else:
        messages.error(request, "Categoría no válida.")
        return redirect("marketplace_list")
    
    producto = get_object_or_404(model, pk=pk)
    if producto.vendedor != request.user:
        messages.error(request, "No tienes permiso para marcar este producto como vendido.")
        return redirect("marketplace_list")
    
    producto.vendido = True
    producto.save()
    messages.success(request, f"¡El producto '{producto.titulo}' se ha marcado como vendido!")
    return redirect("marketplace_list")
