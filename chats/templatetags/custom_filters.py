from django import template

register = template.Library()

@register.filter
def endswith(value, arg):
    """
    Devuelve True si el string 'value' termina con el substring 'arg'.
    """
    try:
        return str(value).lower().endswith(str(arg).lower())
    except Exception:
        return False