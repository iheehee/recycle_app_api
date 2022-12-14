# Generated by Django 4.1.2 on 2022-11-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0027_delete_challengeapply"),
        ("users", "0007_alter_profile_has_challenge"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="has_challenge",
            field=models.ManyToManyField(default="", to="challenges.challenge"),
        ),
    ]
