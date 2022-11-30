from django import template
from promo.models import *

register = template.Library()


@register.simple_tag(name='getcity')
def get_cities(filter=None):
    if not filter:
        return Cities.objects.all()
    else:
        return Cities.objects.filter(pk=filter)


@register.inclusion_tag('promo/list_cities.html')
def show_cities(sort=None, cits_selected=0):
    if not sort:
        cits = Cities.objects.all()
    else:
        cits = Cities.objects.order_by(sort)
    return {"cits": cits, "cits_selected": cits_selected}
