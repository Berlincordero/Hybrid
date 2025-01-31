from django.contrib.messages import constants as messages
from pathlib import Path
import environ
from django.utils.translation import gettext_lazy as _
import os

# Configuración de variables de entorno
env = environ.Env()
environ.Env.read_env()

# Definir BASE_DIR como un objeto Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = env('SECRET_KEY', default='tu_clave_secreta_aquí')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = ['*']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',
    'widget_tweaks',
    'config',          # Asegúrate de que 'config' esté incluido
    'Administrador',
    'Perfiles',
    'Friends',
    'chats',
    'opiniones',
    'Medios',
    'Marketplace',
    'Foro',
    'subasta',
    'Notificacion',
    'Fincas',
    'panel',
    'comunity',
    'galeria',
    'vivero',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'axes.middleware.AxesMiddleware',  # Middleware de django-axes
    'django.middleware.locale.LocaleMiddleware',  # Debe estar después de SessionMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',  # Backend de django-axes para protección contra fuerza bruta
    'django.contrib.auth.backends.ModelBackend',  # Backend de autenticación predeterminado de Django
]


MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}



# Configuración de django-axes
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1
AXES_USE_IP_ADDRESS = False
AXES_RESET_ON_SUCCESS = True
AXES_FAILURE_LIMITING_BY_USER_AND_IP = False
AXES_FAILURE_LIMITING_BY_USER = True
AXES_LOCK_OUT_AT_FAILURE = True
AXES_USERNAME_CALLABLE = 'Administrador.utils.get_email_as_username'
AXES_HANDLER = 'axes.handlers.database.AxesDatabaseHandler'
AXES_VERBOSE = True

# Desde el archivo .env


# Configuración de URLs
ROOT_URLCONF = 'config.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Usar '/' con objetos Path
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Necesario para i18n
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n', 
                'Perfiles.context_processors.user_profile_context',
                'Foro.context_processors.foros_context_processor',
            ],
        },
    },
]

# Aplicación WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# Configuración de bases de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fincahub',  # Nombre de la base de datos
        'USER': 'postgres',
        'PASSWORD': 'kik301',
        'HOST': 'localhost',  # o la dirección de tu servidor PostgreSQL
        'PORT': '5432',  # el puerto por defecto de PostgreSQL es 5432
    }
}

# Configuraciones de validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,  # Puedes ajustar la longitud mínima
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Configuración para redirigir después de iniciar sesión
LOGIN_REDIRECT_URL = 'index'  # Asegúrate de tener una URL llamada 'index'
LOGOUT_REDIRECT_URL = 'login_view'


LANGUAGE_CODE = 'es'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Definir los idiomas disponibles

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Español')),
    ('fr', _('Français')),
    ('pt', _('Português')),      # Portugués
    ('de', _('Deutsch')),        # Alemán       
    # Agrega más idiomas si es necesario
]
# Rutas de locales
LOCALE_PATHS = [
    BASE_DIR / 'locale',  # Usar '/' con objetos Path
]

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Usar '/' con objetos Path
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Usar '/' con objetos Path

# Campo clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP de Gmail
EMAIL_PORT = 587  # Puerto para conexiones TLS
EMAIL_USE_TLS = True  # Activa TLS
EMAIL_HOST_USER = 'enriquecorderob33@gmail.com'  # Tu correo de administrador
EMAIL_HOST_PASSWORD = 'fincahub93'  # Tu contraseña o contraseña de aplicación

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'