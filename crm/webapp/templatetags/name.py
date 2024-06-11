from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr_name):
    _name = []
    for name in attr_name.split():
        _name.append(str(getattr(obj, name)))
    return ' '.join(_name)