# Generated by Django 4.2.1 on 2023-09-01 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0057_alter_challengecertification_challenge_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengecertification',
            name='challenge_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='certification_challenge', to='challenges.challengeapply', verbose_name='challenge name'),
        ),
    ]
