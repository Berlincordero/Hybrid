from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Grupo, Publicacion, Comentario
from .forms import GrupoForm, PublicacionForm, ComentarioForm

@login_required
def listar_grupos(request):
    """Lista todos los grupos disponibles."""
    grupos = Grupo.objects.all()
    return render(request, 'community/listar_grupos.html', {'grupos': grupos})

@login_required
def detalle_grupo(request, grupo_id):
    """Muestra el detalle de un grupo específico."""
    grupo = get_object_or_404(Grupo, id=grupo_id)
    publicaciones = grupo.publicaciones.all()
    return render(request, 'community/detalle_grupo.html', {'grupo': grupo, 'publicaciones': publicaciones})

@login_required
def crear_grupo(request):
    """Permite a los usuarios crear un grupo."""
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.administrador = request.user
            grupo.save()
            grupo.miembros.add(request.user)
            return redirect('listar_grupos')
    else:
        form = GrupoForm()
    return render(request, 'community/crear_grupo.html', {'form': form})

@login_required
def crear_publicacion(request, grupo_id):
    """Crea una publicación dentro de un grupo."""
    grupo = get_object_or_404(Grupo, id=grupo_id)
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.grupo = grupo
            publicacion.autor = request.user
            publicacion.save()
            return redirect('detalle_grupo', grupo_id=grupo.id)
    else:
        form = PublicacionForm()
    return render(request, 'community/crear_publicacion.html', {'form': form, 'grupo': grupo})

@login_required
def agregar_comentario(request, publicacion_id):
    """Agrega un comentario a una publicación."""
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_grupo', grupo_id=publicacion.grupo.id)
    else:
        form = ComentarioForm()
    return render(request, 'community/agregar_comentario.html', {'form': form, 'publicacion': publicacion})
