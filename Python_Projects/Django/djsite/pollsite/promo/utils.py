from django.db.models import *
from django.core.cache import cache
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить кампанию", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cits = cache.get('cits')
        if not cits:
            cits = Cities.objects.annotate(Count('promo'))
            cache.set('cits', cits, 60)

        cits = Cities.objects.annotate(Count('promo'))

        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cits

        if 'cits_selected' not in context:
            context['cits_selected'] = 0
        return context
