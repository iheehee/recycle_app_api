from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {"fields": ("avatar", "favs")},
        ),
    )
    list_display = ("username", "email","nick_name")

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("user", "nickname")
