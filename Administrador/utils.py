from django.core.exceptions import ImproperlyConfigured

def get_email_as_username(request, credentials):
    """
    Utiliza el email como identificador principal para rastrear intentos fallidos en django-axes.
    """
    # Verifica si la clave 'email' está en las credenciales
    if credentials and 'email' in credentials:
        return credentials['email']
    # Alternativamente, busca el email en los datos POST de la solicitud
    if request and request.POST:
        return request.POST.get('email', None)
    return None




def get_client_ip(request):
    """
    Obtiene la dirección IP del cliente desde el encabezado de la solicitud.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    if not ip:
        raise ImproperlyConfigured("No se pudo determinar la dirección IP del cliente.")
    
    return ip
