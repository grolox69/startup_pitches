from django import template

register = template.Library()


def rep(value):
    return value.replace("watch?v=", "embed/")


def cut(value, arg):
    return value.replace(arg, '')


register.filter('rep', rep)
register.filter('cut', cut)
