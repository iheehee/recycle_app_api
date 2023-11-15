from django.db import models
from django.core.validators import MaxValueValidator
from core.models import Core


class Challenge(Core):
    FREQUENCY = (
        ("주 1일", 1),
        ("주 2일", 2),
        ("주 3일", 3),
        ("주 4일", 4),
        ("주 5일", 5),
        ("주 6일", 6),
        ("주 7일", 7),
        ("평일 매일", 8),
        ("주말 매일", 9),
    )
    DURATIONS = (
        ("1주 동안", 1),
        ("2주 동안", 2),
        ("3주 동안", 3),
        ("4주 동안", 4),
    )

    title = models.CharField(max_length=140, default="", blank=True)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="owner", null=True
    )
    title_banner = models.ImageField(
        upload_to="title_banner", default="", blank=True, null=True
    )
    summery = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    start_day = models.DateField(null=True)
    frequency = models.CharField(max_length=50, choices=FREQUENCY, default="")
    duration = models.CharField(max_length=50, choices=DURATIONS, null=True)
    certifications = models.ManyToManyField(
        "ChallengeCertification", related_name="Certifications"
    )
    certifications_start_time = models.CharField(max_length=30, default="", blank=True)
    certifications_end_time = models.CharField(max_length=30, default="", blank=True)
    certification_notice = models.TextField(blank=True)
    success_photo_example = models.ManyToManyField("SuccessPhotoExample", default="")
    fail_photo_example = models.ManyToManyField("FailPhotoExample", default="")
    member = models.ManyToManyField(
        "users.Profile",
        through="ChallengeApply",
    )
    max_member = models.IntegerField(default=1, validators=[MaxValueValidator(20)])
    number_of_applied_member = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class SuccessPhotoExample(models.Model):
    challenge_name = models.ForeignKey(
        "Challenge",
        related_name="challenge_success_photo",
        verbose_name="challenge name",
        on_delete=models.CASCADE,
        null=True,
    )
    success_photo = models.ImageField(
        upload_to="success_photo_ex",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )


class FailPhotoExample(models.Model):
    challenge_name = models.ForeignKey(
        "Challenge",
        related_name="challenge_fail_photo",
        verbose_name="challenge name",
        on_delete=models.CASCADE,
        null=True,
    )
    fail_photo = models.ImageField(
        upload_to="fail_photo_ex",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )


class ChallengeApply(models.Model):
    challenge_id = models.ForeignKey(
        "Challenge",
        verbose_name="challenge name",
        on_delete=models.CASCADE,
        related_name="challenge_name",
        default="",
    )
    member_id = models.ForeignKey(
        "users.Profile",
        verbose_name="member name",
        on_delete=models.CASCADE,
        related_name="member_name",
        default="",
    )

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.challenge_id)


class ChallengeCertification(models.Model):
    certification_id = models.AutoField(primary_key=True)
    challenge_id = models.ForeignKey(
        "Challenge",
        verbose_name="challenge name",
        on_delete=models.CASCADE,
        related_name="certification_challenge",
        default="",
    )
    participant_id = models.ForeignKey(
        "users.Profile",
        verbose_name="member name",
        on_delete=models.CASCADE,
        related_name="participant",
        default="",
    )
    certification_date = models.DateTimeField(auto_now=True)
    certification_photo = models.FileField(
        upload_to="certification", blank=True, default=""
    )
    certification_comment = models.CharField(max_length=255, blank=True)


class ChallengeReview(models.Model):
    rating = models.IntegerField(null=True)
    comment = models.CharField(max_length=100, default="")
    challenge = models.ManyToManyField(
        "Challenge",
        verbose_name="review",
        related_name="review",
    )
