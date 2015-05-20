from django.contrib import admin

from .models import Hotel, Galery, Ranking


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_filter = ['name']
    search_fields = ['description']


class GaleryAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'description_text')
    list_filter = ['hotel']
    search_fields = ['hotel']


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Galery, GaleryAdmin)
