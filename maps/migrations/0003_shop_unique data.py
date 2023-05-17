# Generated by Django 4.1.5 on 2023-01-13 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0002_category_alter_shop_lat_alter_shop_lng_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="shop",
            constraint=models.UniqueConstraint(
                fields=("name", "address"), name="unique data"
            ),
        ),
    ]