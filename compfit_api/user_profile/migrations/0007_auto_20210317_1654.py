# Generated by Django 3.1.5 on 2021-03-17 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20210307_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workoutplaylist',
            old_name='owner_id',
            new_name='owner',
        ),
    ]