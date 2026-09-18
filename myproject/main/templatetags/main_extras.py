from django import template

register = template.Library()


@register.filter
def capitalize(value):
    value = str(value)
    return value[:1].upper() + value[1:]
