from django.contrib import admin

from .models import Category, Brand, Bike


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Bike)