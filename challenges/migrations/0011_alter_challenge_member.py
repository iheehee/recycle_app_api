# Generated by Django 4.1.2 on 2022-11-03 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("challenges", "0010_alter_challenge_member"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="member",
            field=models.ManyToManyField(
                default="", related_name="member", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
