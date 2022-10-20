from django.contrib import admin
from . import models


@admin.register(models.Challenge)
class RecycleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "owner",
        "title_banner",
        "challenge_summery",
        "description",
        "start_day",
        "end_day",
        "certification_success_photo_example",
        "certification_fail_photo_example",
        "certification_notice",
        "count_members",
    )
    def count_members(self, obj):
        return obj.members.all().count()
    
   
    
