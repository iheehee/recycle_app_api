# Generated by Django 4.2.1 on 2023-11-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0062_alter_challenge_certification_photo_example'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='certification_photo_example',
            field=models.ManyToManyField(default='', related_name='CertificationExample', to='challenges.certificationexample'),
        ),
    ]
