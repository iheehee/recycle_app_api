from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    
    #fieldsets = UserAdmin.fieldsets + (
    #   (
    #        "Custom Profile",
    #        {"fields": ("avatar","favs")},
    #    ),
    #)
    list_display = ("email", "nickname",)


