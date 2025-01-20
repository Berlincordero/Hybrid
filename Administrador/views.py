
from django.shortcuts import render, redirect
from datetime import date
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect  # <--- Asegúrate de agregar esta línea
from django.core.mail import send_mail
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from axes.utils import reset
from Administrador.utils import get_client_ip


def mas_informacion(request):
    return render(request, 'mas_informacion.html')



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    # Resetea intentos fallidos para el usuario
                    reset(username=user.username)
                    auth_login(request, user)
                    return redirect('index')
                else:
                    messages.error(request, "Credenciales inválidas.")
            except User.DoesNotExist:
                messages.error(request, "No existe un usuario con este correo electrónico.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """
    Vista para manejar el cierre de sesión.
    """
    logout(request)
    return redirect('login_view')  # Asegúrate de que 'login_view' esté correctamente configurada en URLs

@csrf_protect
def register(request):
    if request.method == 'POST':
        # Extraer datos del formulario
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        birth_day = request.POST.get('birth_day')
        birth_month = request.POST.get('birth_month')
        birth_year = request.POST.get('birth_year')
        gender = request.POST.get('gender')

        # Validaciones básicas
        errors = []

        if not first_name:
            errors.append("El campo Nombre es obligatorio.")
        if not last_name:
            errors.append("El campo Apellido es obligatorio.")
        if not email:
            errors.append("El campo Correo Electrónico es obligatorio.")
        if not password:
            errors.append("El campo Contraseña es obligatorio.")
        if not gender:
            errors.append("El campo Género es obligatorio.")

        # Validar formato de correo electrónico
        if email:
            from django.core.validators import validate_email
            from django.core.exceptions import ValidationError
            try:
                validate_email(email)
                if User.objects.filter(email=email).exists():
                    errors.append("El correo ya está registrado.")
            except ValidationError:
                errors.append("Formato de correo electrónico inválido.")

        # Validar fecha de nacimiento
        birth_date = None
        if birth_day and birth_month and birth_year:
            try:
                birth_date = date(int(birth_year), int(birth_month), int(birth_day))
            except ValueError:
                errors.append("Fecha de nacimiento inválida.")
        else:
            errors.append("Todos los campos de Fecha de nacimiento son obligatorios.")

        # Validar contraseña (puedes agregar más validaciones según tus necesidades)
        if len(password) < 8:
            errors.append("La contraseña debe tener al menos 8 caracteres.")

        if errors:
            for error in errors:
                messages.error(request, error)
            # Mantener los valores ingresados en el formulario
            context = {
                'days': range(1, 32),
                'months': [
                    (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
                    (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
                    (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
                ],
                'years': range(1900, 2026)[::-1],
                'previous_data': request.POST
            }
            return render(request, 'register.html', context)

        # Crear usuario
        username_base = f"{first_name.lower()}.{last_name.lower()}"
        username = username_base
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{username_base}{counter}"
            counter += 1

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Actualizar perfil
        if birth_date:
            user.profile.birth_date = birth_date
        if gender:
            user.profile.gender = gender
        user.profile.save()

        # **Asignar el backend antes de iniciar sesión**
        user.backend = 'django.contrib.auth.backends.ModelBackend'

        # Iniciar sesión automáticamente después del registro
        auth_login(request, user)
        messages.success(request, "Registro exitoso. ¡Bienvenido(a)!")
        return redirect('index')  # Asegúrate de tener una URL llamada 'index'
    else:
        context = {
            'days': range(1, 32),
            'months': [
                (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
                (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
                (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
            ],
            'years': range(1900, 2026)[::-1],
        }
        return render(request, 'register.html', context)
def condiciones_uso(request):
    return render(request, 'condiciones_uso.html')

def politica_privacidad(request):
    return render(request, 'politica_privacidad.html')

def politica_cookies(request):
    return render(request, 'politica_cookies.html')

def enviar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        mensaje_completo = f"Nombre: {nombre}\nCorreo: {correo}\n\nMensaje:\n{mensaje}"

        try:
            # Envía un correo al administrador
            send_mail(
                asunto,  # Asunto
                mensaje_completo,  # Cuerpo del mensaje
                'enriquecorderob33@gmail.com',  # Remitente (puede ser el correo del usuario o fijo)
                ['enriquecorderob33@gmail.com'],  # Destinatario (tu correo de administrador)
            )
            messages.success(request, 'Tu mensaje ha sido enviado exitosamente.')
        except Exception as e:
            messages.error(request, f'Error al enviar el mensaje: {str(e)}')

        return redirect('register')  # Redirige a la página principal o donde desees
    return render(request, 'contacto.html')

def lockout(request):
    return render(request, 'lockout.html')


