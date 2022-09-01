from django.db import models
from core.models import Core


class Recycle(Core):

    CATEGORIES = (
        ("LOGIN_EMAIL", "가구"),
        ("LOGIN_GITHUB", "생활용품"),
        ("LOGING_KAKAO", "도서"),
    )

    name = models.CharField(max_length=140, default="")
    how_to_recyle = models.TextField()
    tip = models.TextField()
    category = models.CharField(choices=CATEGORIES, blank=True, max_length=40)

    def __str__(self):
        return self.name