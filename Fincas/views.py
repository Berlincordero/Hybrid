from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Finca
from .forms import FincaForm

@login_required
def listar_fincas(request):
    """Lista todas las fincas del usuario autenticado."""
    fincas = Finca.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'listar_fincas.html', {'fincas': fincas})

@login_required
def crear_finca(request):
    """Crea una nueva finca."""
    if request.method == 'POST':
        form = FincaForm(request.POST, request.FILES)
        if form.is_valid():
            finca = form.save(commit=False)
            finca.usuario = request.user
            finca.save()
            return redirect('listar_fincas')
    else:
        form = FincaForm()
    return render(request, 'crear_finca.html', {'form': form})

@login_required
def eliminar_finca(request, finca_id):
    finca = get_object_or_404(Finca, id=finca_id, usuario=request.user)
    if request.method == 'POST':
        finca.delete()
        return redirect('listar_fincas')
    # Opcionalmente puedes mostrar una página de confirmación
    return render(request, 'confirmar_eliminar_finca.html', {'finca': finca})