from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Foro, Comentario
from .forms import ForoForm, ComentarioForm
# Foro/views.py
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Foro
from .forms import ForoForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from .models import Foro
from .forms import ComentarioForm

@login_required
def foro_list(request):
    """
    Muestra todos los foros de un usuario en una sola página (feed),
    con la información completa (texto, imagen o video),
    comentarios y acciones (estrella, repost).
    """
    # Filtra solo foros cuyo autor sea el usuario actual
    foros = Foro.objects.filter(autor=request.user).order_by('-created_at')

    # Formulario de comentario vacío (se usará para cada foro)
    comentario_form = ComentarioForm()

    context = {
        "foros": foros,
        "comentario_form": comentario_form,
    }
    return render(request, "foro_list.html", context)

@login_required
def foro_create(request):
    """
    Vista para crear un nuevo foro en una página separada
    (en caso no quieras crearlo dentro de la misma lista).
    """
    if request.method == "POST":
        form = ForoForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_foro = form.save(commit=False)
            nuevo_foro.autor = request.user
            nuevo_foro.save()
            return redirect("foro_list")
    else:
        form = ForoForm()
    
    return render(request, "foro_create.html", {"form": form})

@login_required
def add_comentario(request, pk):
    """
    Agrega un comentario al foro especificado en pk
    y redirige de nuevo a la lista de foros.
    """
    foro = get_object_or_404(Foro, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.foro = foro
            comentario.save()
    return redirect("index")

@login_required
def toggle_estrella(request, pk):
    """
    Marca o desmarca la estrella en un foro (similar a un "like")
    y regresa a la lista de foros.
    """
    foro = get_object_or_404(Foro, pk=pk)
    user = request.user
    if user in foro.estrellas.all():
        foro.estrellas.remove(user)
    else:
        foro.estrellas.add(user)
    return redirect("index")

@login_required
def repost_foro(request, pk):
    """
    Crea un nuevo post como 'repost' del foro original.
    Copia el contenido y marca el campo reposted=True.
    """
    original = get_object_or_404(Foro, pk=pk)
    Foro.objects.create(
        autor=request.user,
        titulo=original.titulo + " (Repost)",
        contenido_texto=original.contenido_texto,
        imagen=original.imagen,
        video=original.video,
        post_type=original.post_type,
        reposted=True,
    )
    return redirect("index")

def foro_feed(request):
    """
    Retorna el HTML parcial (_foro_cards.html) dentro de un JSON
    para refrescar dinámicamente el feed.
    """
    foros = Foro.objects.all().order_by('-created_at')
    comentario_form = ComentarioForm()

    html_cards = render_to_string(
        '_foro_cards.html',
        {
            'foros': foros,
            'comentario_form': comentario_form,
        },
        request=request
    )
    return JsonResponse({'html': html_cards})

