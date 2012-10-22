from django import template

register = template.Library()

@register.filter(name='getMonth')
def getMonth(value):

    return value.strftime("%b")
