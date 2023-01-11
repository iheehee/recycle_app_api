from django.db import models


class Maps(models.Model):
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    tel = models.CharField(max_length=140)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)


class Shop(models.Model):
    category = models.CharField(max_length=140)
