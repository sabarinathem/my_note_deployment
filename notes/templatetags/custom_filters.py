from django import template

register = template.Library()

@register.filter
def lines_to_list(value):
    return value.splitlines()
