from django.contrib import admin
from . models import Car

# Register your models here.

class CarModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'status',
    )
admin.site.register(Car, CarModelAdmin)