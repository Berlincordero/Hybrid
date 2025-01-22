from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Subasta, Oferta
from .forms import SubastaForm, OfertaForm

@login_required
def listar_subastas(request):
    # Obtener todas las subastas activas
    subastas = Subasta.objects.filter(fecha_fin__gte=now()).order_by('fecha_fin')
    oferta_forms = {}  # Diccionario para manejar un formulario por subasta

    # Manejo de ofertas
    if request.method == 'POST':
        subasta_id = request.POST.get('subasta_id')
        subasta = Subasta.objects.get(id=subasta_id)
        form = OfertaForm(request.POST)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.subasta = subasta
            oferta.comprador = request.user
            oferta.save()
            return redirect('listar_subastas')

    # Crear formularios vacíos para cada subasta
    for subasta in subastas:
        oferta_forms[subasta.id] = OfertaForm()

    return render(request, 'listar_subastas.html', {
        'subastas': subastas,
        'oferta_forms': oferta_forms,
    })


@login_required
def crear_subasta(request):
    if request.method == 'POST':
        form = SubastaForm(request.POST, request.FILES)
        if form.is_valid():
            subasta = form.save(commit=False)
            subasta.vendedor = request.user
            subasta.save()
            return redirect('listar_subastas')
    else:
        form = SubastaForm()

    return render(request, 'crear_subasta.html', {'form': form})
