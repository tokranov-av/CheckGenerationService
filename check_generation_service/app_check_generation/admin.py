from django.contrib import admin
from .models import Printer, Check


@admin.register(Printer)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'api_key', 'check_type', 'point_id')
    ordering = ('id',)
    list_display_links = ('id', 'name',)
    search_fields = ('point_id',)
    list_filter = ('point_id',)


@admin.register(Check)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'printer', 'type', 'order', 'status', 'pdf_file')
    ordering = ('id',)
    list_display_links = ('id',)
    list_filter = ('printer', 'type', 'status',)
