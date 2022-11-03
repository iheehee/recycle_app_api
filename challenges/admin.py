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
        "count_members",
    )
    def count_members(self, obj):
        return obj.member.all().count()
    
@admin.register(models.ChallengeMember)
class ChallengeMemberAdmin(admin.ModelAdmin):

    list_display = (
        "challenge_name",
        "member",
    )
   
    
