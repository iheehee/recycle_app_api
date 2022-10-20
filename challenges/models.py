from distutils import text_file
from django.db import models
from core.models import Core


class Challenge(Core):

    title = models.CharField(max_length=140, default="")
    owner = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="challenge_owner")
    title_banner = models.ImageField(upload_to="title_banner", default="",blank=True)
    challenge_summery = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    start_day = models.TimeField()
    end_day = models.TimeField()
    certification_success_photo_example = models.ImageField(
        verbose_name="success photo",
        upload_to="success_photo_ex",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True
    )
    certification_fail_photo_example = models.ImageField(
        verbose_name="fail photo",
        upload_to="success_fail_ex",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True
    )
    certification_notice = models.TextField(blank=True)
    members = models.ManyToManyField("users.User", default="", related_name="challenge_member")



    def __str__(self):
        return self.title
