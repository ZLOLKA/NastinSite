from django import template

register = template.Library()


@register.filter(is_safe=True)
def addstr(arg1, arg2):
    return str(arg1) + str(arg2)
