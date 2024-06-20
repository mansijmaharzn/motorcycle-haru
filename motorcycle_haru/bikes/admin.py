from django.contrib import admin

from .models import Category, Brand, Bike


class BikeAdmin(admin.ModelAdmin):
    list_display= ('name', 'brand', 'category', 'owner')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Bike, BikeAdmin)

#admin fields for data showing in admin panel