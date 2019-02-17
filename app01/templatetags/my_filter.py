from django import template

register = template.Library()  # register的名字不能改


@register.filter
def add_dsb(value, arg):
    return "{}_{}".format(value, arg)
