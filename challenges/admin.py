from django.contrib import admin
from . import models


@admin.register(models.Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "owner",
        "title_banner",
        "summery",
        "description",
        "start_day",
        "certification_notice",
    )


@admin.register(models.SuccessPhotoExample)
class SuccessPhotoExample(admin.ModelAdmin):
    list_display = ("challenge_name", "success_photo", "owner")


@admin.register(models.FailPhotoExample)
class FailPhotoExample(admin.ModelAdmin):
    list_display = (
        "challenge_name",
        "fail_photo",
        "owner",
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
        "certification_id",
        "challenge_id",
        "participant_id",
        "certification_date",
        "certification_photo",
        "certification_comment",
    )
