from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
def addstr(arg1, arg2):
    return arg1 + arg2
