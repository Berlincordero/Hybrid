from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Archivo
from .forms import ArchivoForm

@login_required
def listar_archivos(request):
    """Lista todos los archivos del usuario autenticado."""
    archivos = Archivo.objects.filter(usuario=request.user)
    return render(request, 'listar_archivos.html', {'archivos': archivos})

@login_required
def subir_archivo(request):
    """Permite al usuario subir un archivo."""
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.usuario = request.user
            archivo.save()
            return redirect('listar_archivos')
    else:
        form = ArchivoForm()
    return render(request, 'galeria/subir_archivo.html', {'form': form})

@login_required
def detalle_archivo(request, archivo_id):
    """Muestra los detalles de un archivo específico."""
    archivo = get_object_or_404(Archivo, id=archivo_id, usuario=request.user)
    return render(request, 'detalle_archivo.html', {'archivo': archivo})
