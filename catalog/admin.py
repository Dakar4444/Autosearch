from django.contrib import admin
from catalog.models import Catalogs, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = "catalogs"
    model = Gallery


class CatalogsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    search_fields = ['gos_number', 'data_photo']
    list_display = ('gos_number', 'data_photo', 'is_approved')

admin.site.register(Catalogs, CatalogsAdmin)