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
        "certification_notice",
    )


@admin.register(models.CertificationExample)
class CertificationExampleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "certification_photo_example",
        "SuccessOrFail",
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
