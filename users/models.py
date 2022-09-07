from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    avatar = models.FileField(upload_to="avatar", black=True)
    favs = models.ManyToManyField("Recycles.Recycle", related_name="favs", blank=True)

    def __str__(self):
        return self.name