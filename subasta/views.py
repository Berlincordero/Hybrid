# subasta/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Subasta, Oferta, SubastaImagen
from .forms import SubastaForm, OfertaForm

@login_required
def listar_subastas(request):
    """
    Muestra las subastas cuya fecha de fin es >= ahora.
    Además permite hacer ofertas vía POST.
    """
    subastas = Subasta.objects.filter(fecha_fin__gte=now()).order_by('fecha_fin')

    # Categorías únicas
    categorias = sorted(set(subastas.values_list('tipo', flat=True)))

    # Un form de oferta por cada subasta
    oferta_forms = {subasta.id: OfertaForm() for subasta in subastas}

    # Si envían oferta vía POST:
    if request.method == 'POST':
        subasta_id = request.POST.get('subasta_id')
        subasta_obj = get_object_or_404(Subasta, id=subasta_id)
        form = OfertaForm(request.POST)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.subasta = subasta_obj
            oferta.comprador = request.user
            oferta.save()
            return redirect('listar_subastas')

    return render(request, 'listar_subastas.html', {
        'subastas': subastas,
        'categorias': categorias,
        'oferta_forms': oferta_forms
    })


@login_required
def crear_subasta(request):
    if request.method == 'POST':
        form = SubastaForm(request.POST, request.FILES)
        if form.is_valid():
            subasta = form.save(commit=False)
            subasta.vendedor = request.user
            subasta.save()

            # Manejar imágenes múltiples
            imagenes = request.FILES.getlist('imagenes')
            for img in imagenes:
                SubastaImagen.objects.create(subasta=subasta, imagen=img)

            return redirect('listar_subastas')
        else:
            # Retornamos la plantilla con los errores del form
            return render(request, 'crear_subasta.html', {'form': form})
    else:
        form = SubastaForm()

    return render(request, 'crear_subasta.html', {'form': form})
