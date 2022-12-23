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
    )


@admin.register(models.ChallengeApply)
class ChallengeApplyAdmin(admin.ModelAdmin):

    list_display = (
        "challenge_id",
        "member_id",
        "created",
    )


@admin.register(models.ChallengeCertification)
class ChallengeCertificationAdmin(admin.ModelAdmin):

    list_display = (
        "challenge_id",
        "challenge_participant_id",
        "certification_date",
        "certification_photo",
        "certification_comment",
    )
