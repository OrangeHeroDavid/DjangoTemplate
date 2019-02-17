from django import template

register = template.Library()  # register的名字不能改


@register.filter
def add_dsb(value, arg='very_dsb'):
    return "{}_{}".format(value, arg)


@register.simple_tag
def add_all(*args, **kwargs):
    return "_".join(args) + '*'.join(kwargs.values())
