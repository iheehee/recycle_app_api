# Generated by Django 4.2.1 on 2023-09-01 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0056_alter_challengecertification_certification_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengecertification',
            name='challenge_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='certification_challenge', to='challenges.challenge', verbose_name='challenge name'),
        ),
    ]