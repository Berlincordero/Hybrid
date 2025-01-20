# Foro/context_processors.py
from .models import Foro
from .forms import ComentarioForm

def foros_context_processor(request):
    """
    Retorna la lista de foros (foros_context) y
    el formulario de comentarios (comentario_form_context)
    para cualquier plantilla.
    """
    foros = Foro.objects.all().order_by('-created_at')
    comentario_form = ComentarioForm()
    return {
        'foros_context': foros,
        'comentario_form_context': comentario_form,
    }
