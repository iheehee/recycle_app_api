# Generated by Django 4.2.1 on 2023-08-31 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_my_certifications'),
        ('challenges', '0053_remove_challengeapply_certification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengeapply',
            name='challenge_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_name', to='challenges.challenge', verbose_name='challenge name'),
        ),
        migrations.AlterField(
            model_name='challengeapply',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_name', to='users.profile', verbose_name='member name'),
        ),
    ]