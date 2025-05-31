from django import template
import calendar

register = template.Library()

# Spanish month names
SPANISH_MONTHS = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
    5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
    9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}

# Spanish day names
SPANISH_DAYS = {
    0: 'Lunes',      # Monday
    1: 'Martes',     # Tuesday  
    2: 'Miércoles',  # Wednesday
    3: 'Jueves',     # Thursday
    4: 'Viernes',    # Friday
    5: 'Sábado',     # Saturday
    6: 'Domingo'     # Sunday
}

@register.filter
def dict_get(dictionary, key):
    """Get item from dictionary by key"""
    if dictionary is None:
        return None
    return dictionary.get(key)

@register.filter
def spanish_day_name(date):
    """Convert date to Spanish day name"""
    if not date:
        return ''
    # Python's weekday() returns 0=Monday, 6=Sunday
    weekday = date.weekday()
    return SPANISH_DAYS.get(weekday, '')

@register.filter  
def spanish_month_name(date):
    """Convert date to Spanish month name"""
    if not date:
        return ''
    month = date.month
    return SPANISH_MONTHS.get(month, '')

@register.filter
def default_if_none_zero(value):
    """Return 0 if value is None"""
    return 0 if value is None else value