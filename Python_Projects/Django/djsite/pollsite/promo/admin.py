from django.contrib import admin
from .models import *


class PromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'camp', 'time_create', 'is_published')
    list_display_links = ('id', 'camp')
    search_fields = ('city', 'camp', 'street')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'city', 'camp')
    prepopulated_fields = {"slug": ("camp",)}


class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class StreetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class HomesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class EntrancesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class FlatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Promo, PromoAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(Streets, StreetsAdmin)
admin.site.register(Homes, HomesAdmin)
admin.site.register(Entrances, EntrancesAdmin)
admin.site.register(Flats, FlatsAdmin)
