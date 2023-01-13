from django.contrib import admin
from . import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "address",
        "tel",
        "lat",
        "lng",
        "image",
        "category_id",
        "borough_id",
    )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "category",
    )


@admin.register(models.Borough)
class BoroughAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "borough",
    )


# Register your models here.
