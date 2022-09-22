from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.FileField(upload_to="avatar", blank=True)
    favs = models.ManyToManyField("recycles.Recycle", related_name="favs", blank=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="profile"
    )
    nickname = models.CharField(max_length=50, blank=True)
