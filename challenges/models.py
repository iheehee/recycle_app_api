from distutils import text_file
import re
from django.db import models
from django.core.validators import MaxValueValidator
from core.models import Core


class Challenge(Core):

    FREQUENCY = (
        ("1time", "주 1회"),
        ("2times", "주 2회"),
        ("3times", "주 3회"),
        ("4times", "주 4회"),
        ("5times", "주 5회"),
        ("6times", "주 6회"),
        ("7times", "매일"),
        ("weekday", "평일 매일"),
        ("weekend", "주말"),
    )
    DURATIONS = (
        ("1week", "1주 동안"),
        ("2weeks", "2주 동안"),
        ("3week", "3주 동안"),
        ("4week", "4주 동안"),
        ("5week", "5주 동안"),
        ("6week", "6주 동안"),
        ("7week", "7주 동안"),
        ("8week", "8주 동안"),
    )

    title = models.CharField(max_length=140, default="", blank=True)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="owner", null=True
    )
    title_banner = models.ImageField(
        upload_to="title_banner", default="", blank=True, null=True
    )
    challenge_summery = models.CharField(max_length=255, blank=True)
    challenge_description = models.TextField(blank=True)
    start_day = models.DateTimeField(null=True)
    frequency = models.CharField(max_length=50, choices=FREQUENCY, default="")
    duration = models.CharField(max_length=50, choices=DURATIONS, null=True)
    certification_success_photo_example = models.ImageField(
        verbose_name="success photo",
        upload_to="success_photo_ex",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )
    certification_fail_photo_example = models.ImageField(
        verbose_name="fail photo",
        upload_to="success_fail_ex",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )
    certification_notice = models.TextField(blank=True)
    max_member = models.IntegerField(default=1, validators=[MaxValueValidator(20)])
    number_of_applied_member = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.title


class ChallengeApply(models.Model):
    challenge_id = models.ForeignKey(
        "Challenge", verbose_name="challenge name", on_delete=models.CASCADE, related_name="challenge_name", null=True
    )
    member_id = models.ForeignKey(
        "users.Profile", verbose_name="member name", on_delete=models.CASCADE, related_name="member_name", null=True
    )
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.challenge_id)



class ChallengeReview(models.Model):
    rating = models.IntegerField(null=True)
    comment = models.CharField(max_length=100, default="")
    challenge = models.OneToOneField(
        "Challenge",
        verbose_name="review",
        on_delete=models.CASCADE,
        related_name="review",
    )
