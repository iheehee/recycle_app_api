# Generated by Django 4.2.1 on 2023-08-31 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0050_alter_challengecertification_certification_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengeapply',
            name='certification',
            field=models.ManyToManyField(null=True, to='challenges.challengecertification'),
        ),
    ]