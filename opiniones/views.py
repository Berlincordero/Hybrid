from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Opinion
from .forms import OpinionForm

@login_required
def opiniones(request):
    if request.method == "POST":
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.autor = request.user
            opinion.save()
            return redirect("opiniones")  # Redirigimos a la misma vista para evitar reenvío de formulario
    else:
        form = OpinionForm()
    
    # Obtenemos todas las opiniones
    opiniones_list = Opinion.objects.all()
    context = {
        "form": form,
        "opiniones": opiniones_list,
    }
    return render(request, "opiniones.html", context)
