from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return '-'.join((new_slug, str(int(time()))))


class Promo(models.Model):
    DOOR_OPEN = [('yes', 'Да'),
                 ('no', 'Нет'),
                 ]
    OPINION = [('positive', 'позитивно',),
               ('neutral', 'нейтрально',),
               ('negative', 'негативно',),
               ]

    camp = models.CharField(max_length=255, unique=True, blank=True, verbose_name='Кампания')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True, verbose_name='URL')
    city = models.ForeignKey('Cities', on_delete=models.PROTECT, verbose_name='Город')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    street = models.ForeignKey('Streets', on_delete=models.PROTECT, verbose_name='Улица')
    home = models.ForeignKey('Homes', on_delete=models.PROTECT, verbose_name='Дом номер')
    entrance = models.ForeignKey('Entrances', on_delete=models.PROTECT, verbose_name='Подъезд номер')
    flat = models.ForeignKey('Flats', on_delete=models.PROTECT, verbose_name='Квартира')
    is_door_open = models.CharField(max_length=50, choices=DOOR_OPEN, verbose_name="Дверь открыли?")
    flat_owner = models.CharField(max_length=255, verbose_name="Владелец квартиры")
    opinion = models.CharField(max_length=50, choices=OPINION, verbose_name="Мнение")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.camp

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.camp)
        super(Promo, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.camp)
    #     super(Promo, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Промо кампания'
        verbose_name_plural = 'Промо кампании'
        ordering = ['-time_create', 'camp']


class Cities(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Город")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cities', kwargs={'city_slug': self.slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['id']


class Streets(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Улица")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    city = models.ForeignKey('Cities', on_delete=models.PROTECT, verbose_name='Город')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('streets', kwargs={'street_slug': self.slug})

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ['id']


class Homes(models.Model):
    name = models.CharField(max_length=25, db_index=True, verbose_name="Дом")
    slug = models.SlugField(max_length=25, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('homes', kwargs={'home_slug': self.slug})

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ['id']


class Entrances(models.Model):
    name = models.CharField(max_length=25, verbose_name="Подъезд")
    slug = models.SlugField(max_length=25, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('entrances', kwargs={'entrance_slug': self.slug})

    class Meta:
        verbose_name = 'Подъезд'
        verbose_name_plural = 'Подъезды'
        ordering = ['id']


class Flats(models.Model):
    name = models.CharField(max_length=25, verbose_name="Квартира")
    slug = models.SlugField(max_length=25, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('flats', kwargs={'flat_slug': self.slug})

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартира'
        ordering = ['id']
