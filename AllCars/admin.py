from django.contrib import admin
from . models import Car, ShowRoom, Bike

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


class BikeModelAdmin(admin.ModelAdmin):
    list_display = (
        'id','name', 'location', 'website'
    )
admin.site.register(Bike, BikeModelAdmin)


class ShowRoomAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'location', 'website'
    )

admin.site.register(ShowRoom, ShowRoomAdmin)