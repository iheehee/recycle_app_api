# Generated by Django 4.1.2 on 2022-10-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0005_remove_challenge_members_challengemember"),
        ("users", "0003_delete_profile"),
    ]

    operations = [
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
                (
                    "avatar",
                    models.FileField(blank=True, default="", upload_to="avatar"),
                ),
                ("has_challenge", models.ManyToManyField(to="challenges.challenge")),
            ],
        ),
    ]
