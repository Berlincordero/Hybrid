from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notificacion

@login_required
def listar_notificaciones(request):
    """Muestra todas las notificaciones del usuario actual."""
    notificaciones = Notificacion.objects.filter(user=request.user).order_by('-fecha_creacion')
    return render(request, 'listar_notificaciones.html', {'notificaciones': notificaciones})

@login_required
def marcar_leido(request, notificacion_id):
    """Marca una notificación como leída."""
    notificacion = get_object_or_404(Notificacion, id=notificacion_id, user=request.user)
    notificacion.leido = True
    notificacion.save()
    if notificacion.enlace:
        return redirect(notificacion.enlace)
    return redirect('listar_notificaciones')
