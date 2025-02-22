# indices/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Indice, LugarRecomendado
from .forms import IndiceForm, LugarRecomendadoForm
from django.contrib import messages
from django.utils import timezone
# indices/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Indice, LugarRecomendado
from .forms import IndiceForm, LugarRecomendadoForm
from django.contrib import messages
from django.utils import timezone


@login_required
def crear_indice(request):
    """
    Crear índice únicamente para Costa Rica.
    """
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder a esta funcionalidad.")
        return redirect("listar_indices")

    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES)
        if form.is_valid():
            indice = form.save(commit=False)
            # Asignamos la fecha actual al crear el índice
            indice.fecha = timezone.now().date()
            # Forzamos a que el índice sea de Costa Rica
            indice.pais = "Costa Rica"
            indice.save()
            messages.success(request, "Índice creado correctamente para Costa Rica.")
            return redirect("listar_indices")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm()

    return render(request, "crear_indice.html", {"form": form})


@login_required
def editar_indice(request, pk):
    """
    Editar únicamente índices de Costa Rica. Si se intenta
    editar otro país, se redirige con un mensaje de error.
    """
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder.")
        return redirect("listar_indices")

    indice = get_object_or_404(Indice, pk=pk)

    # Verificamos que sea de Costa Rica
    if indice.pais != "Costa Rica":
        messages.error(request, "Solo se pueden editar índices de Costa Rica.")
        return redirect("listar_indices")

    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES, instance=indice)
        if form.is_valid():
            # Aunque sea edición, forzamos que siga siendo de Costa Rica
            indice_editado = form.save(commit=False)
            indice_editado.pais = "Costa Rica"
            indice_editado.save()

            messages.success(request, "Índice de Costa Rica actualizado correctamente.")
            return redirect("listar_indices")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm(instance=indice)

    return render(request, "editar_indice.html", {"form": form, "indice": indice})


@login_required
def listar_indices(request):
    """
    Vista para listar únicamente los índices de Costa Rica.
    """
    indices_carnes = Indice.objects.filter(pais="Costa Rica", sub_categoria='carnes').order_by('-fecha')
    indices_granos = Indice.objects.filter(pais="Costa Rica", sub_categoria='granos').order_by('-fecha')
    indices_vegetales = Indice.objects.filter(pais="Costa Rica", sub_categoria='vegetales').order_by('-fecha')
    indices_frutas = Indice.objects.filter(pais="Costa Rica", sub_categoria='frutas').order_by('-fecha')
    indices_lacteos = Indice.objects.filter(pais="Costa Rica", sub_categoria='lacteos').order_by('-fecha')

    context = {
        "indices_carnes": indices_carnes,
        "indices_granos": indices_granos,
        "indices_vegetales": indices_vegetales,
        "indices_frutas": indices_frutas,
        "indices_lacteos": indices_lacteos,
        "country_name": "Costa Rica",
        "flag_url": "img/Bandera_de_costa_rica.png",
        "title": "Índices Económicos de Productos de Costa Rica"
    }
    return render(request, "listar_indices.html", context)


# El resto de tus vistas (lugares, índices de otros países, etc.) se mantienen igual...


@login_required
def listar_lugares_recomendados(request):
    lugares = LugarRecomendado.objects.all().order_by('nombre')
    return render(request, 'listar_lugares_recomendados.html', {'lugares': lugares})

@login_required
def crear_lugar_recomendado(request):
    if request.method == 'POST':
        form = LugarRecomendadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_lugares_recomendados')
    else:
        form = LugarRecomendadoForm()
    return render(request, 'crear_lugar_recomendado.html', {'form': form})


@login_required
def indice_panama(request):
    indices_carnes = Indice.objects.filter(pais="Panamá", sub_categoria="carnes").order_by('-fecha')
    indices_granos = Indice.objects.filter(pais="Panamá", sub_categoria="granos").order_by('-fecha')
    indices_vegetales = Indice.objects.filter(pais="Panamá", sub_categoria="vegetales").order_by('-fecha')
    indices_frutas = Indice.objects.filter(pais="Panamá", sub_categoria="frutas").order_by('-fecha')
    indices_lacteos = Indice.objects.filter(pais="Panamá", sub_categoria="lacteos").order_by('-fecha')

    context = {
        "indices_carnes": indices_carnes,
        "indices_granos": indices_granos,
        "indices_vegetales": indices_vegetales,
        "indices_frutas": indices_frutas,
        "indices_lacteos": indices_lacteos,
        "country_name": "Panamá",
        "flag_url": "img/Bandera_de_panama.png",
        "title": "Índices Económicos de Panamá"
    }
    return render(request, "indice_panama.html", context)

@login_required
def crear_indice_panama(request):
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder a esta funcionalidad.")
        return redirect("indice_panama")
    
    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES)
        if form.is_valid():
            indice = form.save(commit=False)
            indice.fecha = timezone.now().date()
            # Asigna el país automáticamente a Panamá
            indice.pais = "Panamá"
            indice.save()
            messages.success(request, "Índice creado correctamente para Panamá.")
            return redirect("indice_panama")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm()
    
    return render(request, "crear_indice_panama.html", {"form": form})


@login_required
def crear_indice_nicaragua(request):
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder a esta funcionalidad.")
        return redirect("indice_nicaragua")
    
    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES)
        if form.is_valid():
            indice = form.save(commit=False)
            indice.fecha = timezone.now().date()
            # Asignamos el país automáticamente a Nicaragua
            indice.pais = "Nicaragua"
            indice.save()
            messages.success(request, "Índice creado correctamente para Nicaragua.")
            return redirect("indice_nicaragua")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm()
    
    return render(request, "crear_indice_nicaragua.html", {"form": form})


@login_required
def indice_nicaragua(request):
    indices_carnes = Indice.objects.filter(pais="Nicaragua", sub_categoria="carnes").order_by('-fecha')
    indices_granos = Indice.objects.filter(pais="Nicaragua", sub_categoria="granos").order_by('-fecha')
    indices_vegetales = Indice.objects.filter(pais="Nicaragua", sub_categoria="vegetales").order_by('-fecha')
    indices_frutas = Indice.objects.filter(pais="Nicaragua", sub_categoria="frutas").order_by('-fecha')
    indices_lacteos = Indice.objects.filter(pais="Nicaragua", sub_categoria="lacteos").order_by('-fecha')

    context = {
        "indices_carnes": indices_carnes,
        "indices_granos": indices_granos,
        "indices_vegetales": indices_vegetales,
        "indices_frutas": indices_frutas,
        "indices_lacteos": indices_lacteos,
        "country_name": "Nicaragua",
        "flag_url": "img/Bandera_de_nicaragua.png",
        "title": "Índices Económicos de Nicaragua"
    }
    return render(request, "indice_nicaragua.html", context)


@login_required
def crear_indice_el_salvador(request):
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder a esta funcionalidad.")
        return redirect("indice_el_salvador")
    
    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES)
        if form.is_valid():
            indice = form.save(commit=False)
            indice.fecha = timezone.now().date()
            # Asigna el país automáticamente a "El Salvador"
            indice.pais = "El Salvador"
            indice.save()
            messages.success(request, "Índice creado correctamente para El Salvador.")
            return redirect("indice_el_salvador")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm()
    
    return render(request, "crear_indice_el_salvador.html", {"form": form})


@login_required
def indice_el_salvador(request):
    # Filtra los índices según su campo "pais" sea "El Salvador"
    indices_carnes = Indice.objects.filter(pais="El Salvador", sub_categoria="carnes").order_by('-fecha')
    indices_granos = Indice.objects.filter(pais="El Salvador", sub_categoria="granos").order_by('-fecha')
    indices_vegetales = Indice.objects.filter(pais="El Salvador", sub_categoria="vegetales").order_by('-fecha')
    indices_frutas = Indice.objects.filter(pais="El Salvador", sub_categoria="frutas").order_by('-fecha')
    indices_lacteos = Indice.objects.filter(pais="El Salvador", sub_categoria="lacteos").order_by('-fecha')

    context = {
        "indices_carnes": indices_carnes,
        "indices_granos": indices_granos,
        "indices_vegetales": indices_vegetales,
        "indices_frutas": indices_frutas,
        "indices_lacteos": indices_lacteos,
        "country_name": "El Salvador",
        "flag_url": "img/Bandera_de_el_salvador.png",
        "title": "Índices Económicos de El Salvador"
    }
    return render(request, "indice_el_salvador.html", context)


@login_required
def crear_indice_guatemala(request):
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder a esta funcionalidad.")
        return redirect("indice_guatemala")
    
    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES)
        if form.is_valid():
            indice = form.save(commit=False)
            indice.fecha = timezone.now().date()
            # Asignamos el país automáticamente a Guatemala
            indice.pais = "Guatemala"
            indice.save()
            messages.success(request, "Índice creado correctamente para Guatemala.")
            return redirect("indice_guatemala")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm()
    
    return render(request, "crear_indice_guatemala.html", {"form": form})


@login_required
def indice_guatemala(request):
    indices_carnes = Indice.objects.filter(pais="Guatemala", sub_categoria="carnes").order_by('-fecha')
    indices_granos = Indice.objects.filter(pais="Guatemala", sub_categoria="granos").order_by('-fecha')
    indices_vegetales = Indice.objects.filter(pais="Guatemala", sub_categoria="vegetales").order_by('-fecha')
    indices_frutas = Indice.objects.filter(pais="Guatemala", sub_categoria="frutas").order_by('-fecha')
    indices_lacteos = Indice.objects.filter(pais="Guatemala", sub_categoria="lacteos").order_by('-fecha')

    context = {
        "indices_carnes": indices_carnes,
        "indices_granos": indices_granos,
        "indices_vegetales": indices_vegetales,
        "indices_frutas": indices_frutas,
        "indices_lacteos": indices_lacteos,
        "country_name": "Guatemala",
        "flag_url": "img/Bandera_de_guatemala.png",
        "title": "Índices Económicos de Guatemala"
    }
    return render(request, "indice_guatemala.html", context)


@login_required
def crear_indice_mexico(request):
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder a esta funcionalidad.")
        return redirect("indice_mexico")
    
    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES)
        if form.is_valid():
            indice = form.save(commit=False)
            indice.fecha = timezone.now().date()
            # Asignamos el país automáticamente a México
            indice.pais = "México"
            indice.save()
            messages.success(request, "Índice creado correctamente para México.")
            return redirect("indice_mexico")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm()
    
    return render(request, "crear_indice_mexico.html", {"form": form})


@login_required
def indice_mexico(request):
    indices_carnes = Indice.objects.filter(pais="México", sub_categoria="carnes").order_by('-fecha')
    indices_granos = Indice.objects.filter(pais="México", sub_categoria="granos").order_by('-fecha')
    indices_vegetales = Indice.objects.filter(pais="México", sub_categoria="vegetales").order_by('-fecha')
    indices_frutas = Indice.objects.filter(pais="México", sub_categoria="frutas").order_by('-fecha')
    indices_lacteos = Indice.objects.filter(pais="México", sub_categoria="lacteos").order_by('-fecha')

    context = {
        "indices_carnes": indices_carnes,
        "indices_granos": indices_granos,
        "indices_vegetales": indices_vegetales,
        "indices_frutas": indices_frutas,
        "indices_lacteos": indices_lacteos,
        "country_name": "México",
        "flag_url": "img/Bandera_de_mexico.png",
        "title": "Índices Económicos de México"
    }
    return render(request, "indice_mexico.html", context)


@login_required
def crear_indice_honduras(request):
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder a esta funcionalidad.")
        return redirect("indice_honduras")
    
    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES)
        if form.is_valid():
            indice = form.save(commit=False)
            indice.fecha = timezone.now().date()
            # Asigna el país automáticamente a Honduras
            indice.pais = "Honduras"
            indice.save()
            messages.success(request, "Índice creado correctamente para Honduras.")
            return redirect("indice_honduras")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm()
    
    return render(request, "crear_indice_honduras.html", {"form": form})


@login_required
def indice_honduras(request):
    indices_carnes = Indice.objects.filter(pais="Honduras", sub_categoria="carnes").order_by('-fecha')
    indices_granos = Indice.objects.filter(pais="Honduras", sub_categoria="granos").order_by('-fecha')
    indices_vegetales = Indice.objects.filter(pais="Honduras", sub_categoria="vegetales").order_by('-fecha')
    indices_frutas = Indice.objects.filter(pais="Honduras", sub_categoria="frutas").order_by('-fecha')
    indices_lacteos = Indice.objects.filter(pais="Honduras", sub_categoria="lacteos").order_by('-fecha')

    context = {
        "indices_carnes": indices_carnes,
        "indices_granos": indices_granos,
        "indices_vegetales": indices_vegetales,
        "indices_frutas": indices_frutas,
        "indices_lacteos": indices_lacteos,
        "country_name": "Honduras",
        "flag_url": "img/Bandera_de_honduras.png",
        "title": "Índices Económicos de Honduras"
    }
    return render(request, "indice_honduras.html", context)
