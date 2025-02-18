from django.contrib import admin
from . models import Car, ShowRoom

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


# class ShowRoomAdmin(admin.ModelAdmin):
#     class Meta:
#         model = ShowRoom
#         fields = "__all__"
    
# admin.site.register(ShowRoom, ShowRoomAdmin)


class ShowRoomAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'location', 'website'
    )

admin.site.register(ShowRoom, ShowRoomAdmin)