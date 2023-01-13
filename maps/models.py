from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    tel = models.CharField(max_length=140)
    lat = models.DecimalField(max_digits=20, decimal_places=9)
    lng = models.DecimalField(max_digits=20, decimal_places=9)
    image = models.FileField(upload_to="shop_image", blank=True, default="")
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    borough_id = models.ForeignKey("Borough", on_delete=models.CASCADE, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "address"],
                name="unique data",
            ),
        ]


class Category(models.Model):
    category = models.CharField(max_length=140)

    def __str__(self):
        return self.category


class Borough(models.Model):
    borough = models.CharField(max_length=140)

    def __str__(self):
        return self.borough
