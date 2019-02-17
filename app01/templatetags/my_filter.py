from django import template

register = template.Library()  # register的名字不能改


@register.filter
def add_dsb(value, arg='very_dsb'):
    return "{}_{}".format(value, arg)
