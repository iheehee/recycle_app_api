# Generated by Django 4.1.1 on 2022-09-27 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recycles", "0009_alter_photo_trash_name_alter_recycle_category_and_more"),
        ("users", "0003_alter_user_nickname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="avatar",
        ),
        migrations.RemoveField(
            model_name="user",
            name="favs",
        ),
        migrations.RemoveField(
            model_name="user",
            name="nickname",
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(max_length=50, null=True)),
                ("avatar", models.FileField(blank=True, upload_to="avatar")),
                (
                    "Username",
                    models.ForeignKey(
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("fav_category", models.ManyToManyField(to="recycles.recycle")),
                (
                    "favs",
                    models.ManyToManyField(
                        blank=True, related_name="favs", to="recycles.recycle"
                    ),
                ),
            ],
        ),
    ]
