# indices/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Indice
from .forms import IndiceForm

@login_required
def listar_indices(request):
    indices = Indice.objects.all().order_by('-fecha')
    return render(request, 'listar_indices.html', {'indices': indices})
