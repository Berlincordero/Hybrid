
from django.forms.widgets import ClearableFileInput

class ClearableMultipleFileInput(ClearableFileInput):
    """
    Extiende ClearableFileInput para permitir seleccionar múltiples archivos.
    """
    allow_multiple_selected = True
