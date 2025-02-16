# indices/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Indice, LugarRecomendado
from .forms import IndiceForm, LugarRecomendadoForm
from django.contrib import messages
from django.utils import timezone

@login_required
def crear_indice(request):
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder a esta funcionalidad.")
        return redirect("listar_indices")
    
    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES)
        if form.is_valid():
            indice = form.save(commit=False)
            # Asigna la fecha actual al crear el índice
            indice.fecha = timezone.now().date()
            indice.save()
            messages.success(request, "Índice creado correctamente.")
            return redirect("listar_indices")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = IndiceForm()
        # Si deseas ocultar el campo 'fecha' en el formulario, lo eliminas:
        # if "fecha" in form.fields:
        #     del form.fields["fecha"]
    
    return render(request, "crear_indice.html", {"form": form})
@login_required
def editar_indice(request, pk):
    if request.user.email != "enriquecorderob33@gmail.com":
        messages.error(request, "No tienes permiso para acceder.")
        return redirect("listar_indices")
    
    indice = get_object_or_404(Indice, pk=pk)
    
    if request.method == "POST":
        form = IndiceForm(request.POST, request.FILES, instance=indice)
        if form.is_valid():
            form.save()
            messages.success(request, "Índice actualizado correctamente.")
            return redirect("listar_indices")
    else:
        form = IndiceForm(instance=indice)

    return render(request, "editar_indice.html", {"form": form, "indice": indice})



@login_required
def listar_indices(request):
    """
    Vista para listar los índices económicos.
    """
    indices_carnes = Indice.objects.filter(sub_categoria='carnes').order_by('-fecha')
    indices_granos = Indice.objects.filter(sub_categoria='granos').order_by('-fecha')
    indices_vegetales = Indice.objects.filter(sub_categoria='vegetales').order_by('-fecha')
    indices_frutas = Indice.objects.filter(sub_categoria='frutas').order_by('-fecha')
    indices_lacteos = Indice.objects.filter(sub_categoria='lacteos').order_by('-fecha')

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

# El resto de tus vistas (editar, lugares, etc.) se mantienen similares.

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
    context = {
        'country_name': 'Panamá',
        'flag_url': 'img/Bandera_de_panama.png',
        'title': 'Índices Económicos de Panamá'
    }
    return render(request, 'indice_panama.html', context)

@login_required
def indice_nicaragua(request):
    context = {
        'country_name': 'Nicaragua',
        'flag_url': 'img/Bandera_de_nicaragua.png',
        'title': 'Índices Económicos de Nicaragua'
    }
    return render(request, 'indice_nicaragua.html', context)

@login_required
def indice_el_salvador(request):
    context = {
        'country_name': 'El Salvador',
        'flag_url': 'img/Bandera_de_el_salvador.png',
        'title': 'Índices Económicos de El Salvador'
    }
    return render(request, 'indice_el_salvador.html', context)

@login_required
def indice_guatemala(request):
    context = {
        'country_name': 'Guatemala',
        'flag_url': 'img/Bandera_de_guatemala.png',
        'title': 'Índices Económicos de Guatemala'
    }
    return render(request, 'indice_guatemala.html', context)

@login_required
def indice_mexico(request):
    context = {
        'country_name': 'México',
        'flag_url': 'img/Bandera_de_mexico.png',
        'title': 'Índices Económicos de México'
    }
    return render(request, 'indice_mexico.html', context)

@login_required
def indice_honduras(request):
    context = {
        'country_name': 'Honduras',
        'flag_url': 'img/Bandera_de_honduras.png',
        'title': 'Índices Económicos de Honduras'
    }
    return render(request, 'indice_honduras.html', context)
