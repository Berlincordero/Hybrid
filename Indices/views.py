# indices/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Indice
from .forms import IndiceForm
from .models import LugarRecomendado
from .forms import LugarRecomendadoForm

@login_required
def listar_indices(request):
    indices = Indice.objects.all().order_by('-fecha')
    return render(request, 'listar_indices.html', {'indices': indices})


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