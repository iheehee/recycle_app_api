# Generated by Django 4.2.1 on 2023-08-31 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0049_alter_challengeapply_certification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengecertification',
            name='certification_id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False),
        ),
    ]