# Generated by Django 4.1.5 on 2023-03-23 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_rename_nickname_profile_nickname_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
    ]