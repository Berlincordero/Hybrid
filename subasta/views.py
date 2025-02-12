# subasta/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Subasta, Oferta, SubastaImagen
from .forms import SubastaForm, OfertaForm

@login_required
def listar_subastas(request):
    subastas = Subasta.objects.filter(fecha_fin__gte=now()).order_by('fecha_fin')
    categorias = sorted(set(subastas.values_list('tipo', flat=True)))
    oferta_forms = {subasta.id: OfertaForm() for subasta in subastas}

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
            imagenes = request.FILES.getlist('imagenes')
            for img in imagenes:
                SubastaImagen.objects.create(subasta=subasta, imagen=img)
            return redirect('listar_subastas')
        else:
            return render(request, 'crear_subasta.html', {'form': form})
    else:
        form = SubastaForm()
    return render(request, 'crear_subasta.html', {'form': form})

@login_required
def mis_subastas(request):
    subastas = Subasta.objects.filter(vendedor=request.user)
    return render(request, 'mis_subastas.html', {'subastas': subastas})

@login_required
def editar_subasta(request, subasta_id):
    subasta = get_object_or_404(Subasta, id=subasta_id, vendedor=request.user)
    if request.method == 'POST':
        form = SubastaForm(request.POST, request.FILES, instance=subasta)
        if form.is_valid():
            subasta = form.save(commit=False)
            subasta.vendedor = request.user
            subasta.save()
            return redirect('mis_subastas')
    else:
        form = SubastaForm(instance=subasta)
    return render(request, 'editar_subasta.html', {'form': form, 'subasta': subasta})

@login_required
def eliminar_subasta(request, subasta_id):
    subasta = get_object_or_404(Subasta, id=subasta_id, vendedor=request.user)
    if request.method == 'POST':
        subasta.delete()
        return redirect('mis_subastas')
    return render(request, 'eliminar_subasta.html', {'subasta': subasta})

@require_POST
@login_required
def rate_subasta(request, subasta_id):
    """
    Recibe una calificación vía POST y actualiza el promedio.
    Se espera que 'rating' sea un entero entre 1 y 5.
    """
    subasta = get_object_or_404(Subasta, id=subasta_id)
    try:
        new_rating = int(request.POST.get('rating'))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Calificación inválida'}, status=400)

    if new_rating < 1 or new_rating > 5:
        return JsonResponse({'error': 'La calificación debe estar entre 1 y 5'}, status=400)

    total = subasta.rating * subasta.rating_count
    total += new_rating
    subasta.rating_count += 1
    subasta.rating = total / subasta.rating_count
    subasta.save()

    return JsonResponse({'rating': subasta.rating, 'rating_count': subasta.rating_count})
