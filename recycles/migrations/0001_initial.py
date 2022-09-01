# Generated by Django 4.1 on 2022-09-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="recycle",
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
                ("created", models.DateTimeField()),
                ("modified", models.DateTimeField()),
                ("name", models.CharField(default="", max_length=140)),
                ("how_to_recyle", models.TextField()),
                ("tip", models.TextField()),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("LOGIN_EMAIL", "가구"),
                            ("LOGIN_GITHUB", "생활용품"),
                            ("LOGING_KAKAO", "도서"),
                        ],
                        max_length=40,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
