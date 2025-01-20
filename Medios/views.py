from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video, VideoComment
from .forms import VideoForm, CommentForm
from django.db.models import Count

from django.db.models import F

@login_required
def videos_list(request):
    # Mantén tu código original para 'videos', 'top_videos_reproducidos', etc.
    videos = Video.objects.all()
    top_videos_reproducidos = Video.objects.order_by('-vistas')[:10]
    top_videos_estrellas = Video.objects.order_by('-estrellas')[:10]

    # 1) Filtramos videos de categoría BLOGGER
    # 2) Creamos un campo “score” = (estrellas + vistas)
    # 3) Ordenamos por “score” descendente
    # 4) Tomamos los primeros 10
    top_bloger_videos = (
        Video.objects
        .filter(categoria="BLOGGER")
        .annotate(score=F('estrellas') + F('vistas'))
        .order_by('-score')[:10]
    )

    # El resto de categorías las puedes dejar igual
    noticias_consejos_cursos = Video.objects.filter(categoria__in=["NOTICIAS", "CURSOS", "CONSEJOS"])
    bloger = Video.objects.filter(categoria="BLOGGER")
    publicitario_servprof = Video.objects.filter(categoria__in=["PUBLICITARIO","SERVICIOS_PROFESIONALES"])
    personal = Video.objects.filter(categoria="PERSONAL")

    context = {
        "videos": videos,
        "top_videos_reproducidos": top_videos_reproducidos,
        "top_videos_estrellas": top_videos_estrellas,

        # Ajusta aquí: en lugar de "bloggers_con_mas_estrellas",
        # ahora usas "top_bloger_videos"
        "top_bloger_videos": top_bloger_videos,

        "noticias_consejos_cursos": noticias_consejos_cursos,
        "bloger": bloger,
        "publicitario_servprof": publicitario_servprof,
        "personal": personal,
    }
    return render(request, "videos_list.html", context)


@login_required
def video_upload(request):
    # --- Código original intacto ---
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.autor = request.user
            video.save()
            return redirect("videos_list")
    else:
        form = VideoForm()
    context = {
        "form": form
    }
    return render(request, "video_upload.html", context)

@login_required
def video_detail(request, pk):
    """Nueva vista para detallar o reproducir el video y manejar comentarios."""
    video = get_object_or_404(Video, pk=pk)
    # Incrementar las vistas
    video.vistas += 1
    video.save()

    # Manejo de comentarios:
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')  # o como manejes la auth
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comentario = comment_form.save(commit=False)
            comentario.video = video
            comentario.user = request.user
            comentario.save()
            return redirect('video_detail', pk=video.pk)
    else:
        comment_form = CommentForm()

    comments = video.comments.all().order_by('-created_at')

    context = {
        "video": video,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "video_detail.html", context)

@login_required
def video_like(request, pk):
    """
    Nueva vista para sumar 1 estrella (like) al video.
    """
    video = get_object_or_404(Video, pk=pk)
    video.estrellas += 1
    video.save()
    return redirect('video_detail', pk=pk)
