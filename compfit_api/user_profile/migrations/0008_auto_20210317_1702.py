# Generated by Django 3.1.5 on 2021-03-17 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_auto_20210317_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='workout_creator',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='workout_type',
        ),
        migrations.DeleteModel(
            name='PlaylistWorkout',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]