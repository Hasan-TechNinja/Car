from django.contrib import admin
from . models import Brand, Mobile

# Register your models here.

class BrandModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'location',
        'website'
    )
admin.site.register(Brand, BrandModelAdmin)


class MobileModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display',
        'battery_capacity',
        'brand',
    )
admin.site.register(Mobile, MobileModelAdmin)