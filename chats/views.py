from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message
from .forms import MessageForm
from Perfiles.models import Perfil  # Verifica que este import funcione

@login_required
def chat_list(request, user_id=None):
    users = User.objects.exclude(id=request.user.id)
    other_user = None
    perfil = None
    messages = []

    if user_id:
        other_user = get_object_or_404(User, id=user_id)
        try:
            perfil = other_user.perfil
        except:
            perfil = None

        messages = Message.objects.filter(
            Q(sender=request.user, destinatario=other_user) |
            Q(sender=other_user, destinatario=request.user)
        ).order_by('timestamp')

        if request.method == "POST":
            # Incluimos request.FILES para la carga de archivos
            form = MessageForm(request.POST, request.FILES)
            if form.is_valid():
                mensaje = form.save(commit=False)
                mensaje.sender = request.user
                mensaje.destinatario = other_user
                mensaje.save()
                return redirect("chat_list", user_id=user_id)
        else:
            form = MessageForm()
    else:
        form = MessageForm()

    context = {
        "users": users,
        "other_user": other_user,
        "perfil": perfil,
        "messages": messages,
        "form": form,
    }
    return render(request, "chat_list.html", context)
