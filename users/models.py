from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=UserManager.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        u = self.create_user(
            email=email,
            nickname=nickname,
            password=password,
        )
        u.is_admin = True
        u.save(using=self._db)
        return u


class User(AbstractUser):

    models.EmailField(max_length=254)
    avatar = models.FileField(upload_to="avatar", blank=True)
    nickname = models.CharField(max_length=50, blank=False, default="")

    def __str__(self):
        return self.username


class Fav(models.Model):

    favs = models.ManyToManyField(
        "recycles.Recycle", related_name="profile", blank=True
    )
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, default="")
