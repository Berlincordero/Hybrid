# indices/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Indice, LugarRecomendado
from .forms import IndiceForm, LugarRecomendadoForm

@login_required
def listar_indices(request):
    # Esta vista es para Costa Rica y utiliza el template 'listar_indices.html'
    indices = Indice.objects.all().order_by('-fecha')
    context = {
        'indices': indices,
        'country_name': 'Costa Rica',
        'flag_url': 'img/Bandera_de_costa_rica.png',
        'title': 'Índices Económicos de Costa Rica'
    }
    return render(request, 'listar_indices.html', context)

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
