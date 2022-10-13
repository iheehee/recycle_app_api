from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
#from django.contrib.auth import get_user_model


class User(AbstractUser):

    email = models.EmailField(max_length=254, unique=True)
    avatar = models.FileField(upload_to="avatar", blank=True)
    nickname = models.CharField(max_length=50, blank=False, default="")
    favs = models.ManyToManyField("recycles.Recycle", related_name="favs", blank=True)
    #USERNAME_FIELD = 'email' 
    #REQUIRED_FIELDS = []

    def __str__(self):
        return self.username