from django.db import models

class Core(models.Model):

    created = models.DateTimeField(auto_now=False)
    modified = models.DateTimeField(auto_now_add=False)

    class Meta:
        abstract = True
    