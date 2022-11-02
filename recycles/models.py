from django.db import models
from core.models import Core


class Recycle(Core):

    CATEGORIES = (
        ("furniture", "가구"),
        ("household goods", "생활용품"),
        ("book", "도서"),
        ("home appliances", "가전제품"),
        ("cosmetics", "화장품"),
        ("fashion", "패션"),
        ("kitchenware", "주방용품"),
        ("food", "식품"),
        ("container/packaging", "용기/포장재"),
        ("glass", "유리"),
        ("vinyl", "비닐 OTHER"),
        ("plastic", "플라스틱 OTHER"),
        ("rubber", "고무"),
    )

    name = models.CharField(max_length=140, default="")
    how_to_recyle = models.TextField(blank=True)
    tip = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORIES, max_length=40, blank=True)
    category_photo = models.FileField(
        upload_to="category", verbose_name=("category_photo"), default=""
    )
    

    def __str__(self):
        return self.name


class Photo(Core):

    trash_photo = models.FileField(upload_to="recycle")
    trash_name = models.ForeignKey(
        "Recycle",
        verbose_name=("trash name"),
        on_delete=models.CASCADE,
        default=""
    )

    def __str__(self):
        return self.trash_name

