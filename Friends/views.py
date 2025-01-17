from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FriendRequest
from django.db.models import Q


@login_required
def friends_suggestions_view(request):
    """
    Muestra:
    1) Solicitudes de amistad pendientes RECIBIDAS por el usuario (pending_requests).
    2) Sugerencias de usuarios (para enviarles solicitud).
       Si ya existe una solicitud 'pending' del usuario logueado hacia ese usuario, 
       mostraremos "Solicitud Enviada" y un botón para Cancelar.
    """
    user = request.user

    # --- 1) Solicitudes que me enviaron (las que YO tengo que aceptar o rechazar) ---
    pending_requests = FriendRequest.objects.filter(
        to_user=user,
        status='pending'
    )

    # --- 2) Sugerencias: todos los usuarios menos yo mismo (ajusta según tu lógica) ---
    all_users = User.objects.exclude(id=user.id)

    suggestions_with_requests = []
    for u in all_users:
        # Busca si ya existe una solicitud PENDIENTE 
        # desde el user actual hacia 'u'
        fr = FriendRequest.objects.filter(
            from_user=user,
            to_user=u,
            status='pending'
        ).first()

        # Guardo un tuple (usuario, friend_requestEncontradaOSinoNone)
        suggestions_with_requests.append((u, fr))

    return render(
        request,
        'friends_suggestions.html',
        {
            'pending_requests': pending_requests,
            'suggestions_with_requests': suggestions_with_requests, 
        }
    )


@login_required
def send_friend_request_view(request, user_id):
    """
    Envía una solicitud de amistad desde el usuario logueado hacia 'user_id'.
    """
    to_user = get_object_or_404(User, pk=user_id)

    if to_user != request.user:
        # Crear solo si no existe ya una previa en estado pendiente
        FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=to_user,
            status='pending'
        )
    # Redirige a la misma página de sugerencias
    return redirect('friends_suggestions')


@login_required
def accept_friend_request_view(request, request_id):
    """
    Acepta la solicitud de amistad con ID = request_id.
    """
    friend_request = get_object_or_404(FriendRequest, pk=request_id)

    # Verificamos que la solicitud sea para el usuario logueado
    if friend_request.to_user == request.user and friend_request.status == 'pending':
        friend_request.status = 'accepted'
        friend_request.save()
        # Aquí podrías crear un objeto 'Friendship' si lo manejaras en otro modelo,
        # o simplemente considerar que 'status=accepted' significa que son amigos.
    return redirect('friends_suggestions')


@login_required
def reject_friend_request_view(request, request_id):
    """
    Rechaza (o elimina) la solicitud de amistad con ID = request_id.
    """
    friend_request = get_object_or_404(FriendRequest, pk=request_id)

    if friend_request.to_user == request.user and friend_request.status == 'pending':
        # O bien puedes simplemente eliminar el objeto:
        # friend_request.delete()
        # O marcarlo como rechazado:
        friend_request.status = 'rejected'
        friend_request.save()

    return redirect('friends_suggestions')


@login_required
def cancel_friend_request_view(request, request_id):
    """
    Permite al usuario que ENVÍO la solicitud cancelarla si aún está pendiente.
    """
    friend_request = get_object_or_404(FriendRequest, pk=request_id)

    # Verificamos que la solicitud haya sido enviada por el usuario actual
    if friend_request.from_user == request.user and friend_request.status == 'pending':
        # O la marcamos como 'rejected', o la eliminamos directamente:
        # friend_request.status = 'rejected'
        # friend_request.save()
        friend_request.delete()

    return redirect('friends_suggestions')


@login_required
def friends_list_view(request):
    user = request.user
    # Obtener todas las solicitudes aceptadas donde el usuario participa
    accepted_requests = FriendRequest.objects.filter(
        status='accepted'
    ).filter(
        Q(from_user=user) | Q(to_user=user)
    )
    
    # Usamos un set para evitar duplicados
    friends_set = set()
    for fr in accepted_requests:
        # Si el usuario es el que envió la solicitud, el amigo es to_user; de lo contrario, es from_user.
        if fr.from_user == user:
            friends_set.add(fr.to_user)
        else:
            friends_set.add(fr.from_user)
    
    # Convertimos el set a lista (para poder iterarla en la plantilla)
    friends = list(friends_set)
    
    return render(request, 'friends_list.html', {'friends': friends})
