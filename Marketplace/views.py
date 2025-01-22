from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm

def marketplace_list(request):
    productos = Producto.objects.all()
    context = {
        "productos": productos,
    }
    return render(request, "marketplace_list.html", context)

@login_required
def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user
            producto.save()
            return redirect("marketplace_list")
    else:
        form = ProductoForm()
    context = {
        "form": form,
    }
    return render(request, "producto_create.html", context)