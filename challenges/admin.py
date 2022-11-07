from django.contrib import admin
from . import models


@admin.register(models.Challenge)
class ChallengeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "owner",
        "title_banner",
        "challenge_summery",
        "challenge_description",
        "start_day",
        "certification_success_photo_example",
        "certification_fail_photo_example",
        "certification_notice",
        "number_of_member",
    )
    #def count_members(self, obj):
    #    return obj.member.all().count()
    

   
    
