# Generated by Django 4.1.2 on 2022-11-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0008_challengemember"),
        ("users", "0005_profile_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="has_challenge",
            field=models.ManyToManyField(default="", to="challenges.challenge"),
        ),
    ]
