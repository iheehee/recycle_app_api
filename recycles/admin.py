from django.contrib import admin
from . import models


@admin.register(models.Recycle)
class RecycleAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "how_to_recyle",
        "tip",
        "category",
    )
