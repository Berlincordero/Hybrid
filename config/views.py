# index/views.py
# index/views.py
from django.shortcuts import render

def index(request):
    # Solo si necesitas un perfil u otra variable
    perfil = None
    if request.user.is_authenticated:
        perfil = request.user.perfil  # O como tengas definido tu modelo
    
    context = {
        'perfil': perfil
    }
    return render(request, 'index.html', context)

