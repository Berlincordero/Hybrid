from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Foro, Comentario, Reaction, CommentReaction
from .forms import ForoForm, ComentarioForm


@login_required
def foro_list(request):
    """
    Muestra todos los foros de un usuario en una sola página (feed).
    """
    foros = Foro.objects.filter(autor=request.user).order_by('-created_at')
    comentario_form = ComentarioForm()
    context = {
        "foros": foros,
        "comentario_form": comentario_form,
    }
    return render(request, "foro_list.html", context)


@login_required
def foro_create(request):
    """
    Vista para crear un nuevo foro en una página separada.
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
    Agrega un comentario al foro.
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
def repost_foro(request, pk):
    """
    Crea un nuevo post como 'repost' del foro original.
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
    Retorna el HTML parcial (_foro_cards.html) dentro de un JSON para refrescar dinámicamente el feed.
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


@login_required
def reaccionar_foro(request, pk, reaction):
    """
    Permite al usuario hacer o cambiar su reacción a un foro.
    Si ya tenía la misma reacción, la quita (toggle).
    Si tenía otra, la actualiza a la nueva.
    Si no tenía ninguna, la crea.
    """
    foro = get_object_or_404(Foro, pk=pk)
    user = request.user

    # Buscamos si el usuario ya tenía reacción en este foro
    existing_reaction = Reaction.objects.filter(foro=foro, user=user).first()

    if existing_reaction:
        # Si la reacción que existe es la misma -> la eliminamos (toggle off)
        if existing_reaction.reaction_type == reaction:
            existing_reaction.delete()
        else:
            # Diferente -> actualizamos a la nueva
            existing_reaction.reaction_type = reaction
            existing_reaction.save()
    else:
        # Crear la reacción
        Reaction.objects.create(
            foro=foro,
            user=user,
            reaction_type=reaction
        )
    return redirect("index")


@login_required
def reaccionar_comentario(request, comentario_pk, reaction):
    """
    Lógica similar, pero para comentarios.
    """
    comentario = get_object_or_404(Comentario, pk=comentario_pk)
    user = request.user

    existing = CommentReaction.objects.filter(comentario=comentario, user=user).first()

    if existing:
        # toggle off
        if existing.reaction_type == reaction:
            existing.delete()
        else:
            existing.reaction_type = reaction
            existing.save()
    else:
        CommentReaction.objects.create(
            comentario=comentario,
            user=user,
            reaction_type=reaction
        )
    return redirect("index")
