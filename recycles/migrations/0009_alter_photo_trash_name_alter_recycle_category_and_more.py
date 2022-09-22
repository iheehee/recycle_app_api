# Generated by Django 4.1.1 on 2022-09-22 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recycles", "0008_alter_recycle_category_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="trash_name",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="recycles.recycle",
                verbose_name="trash name",
            ),
        ),
        migrations.AlterField(
            model_name="recycle",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
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
                ],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="recycle",
            name="category_photo",
            field=models.FileField(
                default="", upload_to="category", verbose_name="category_photo"
            ),
        ),
    ]
