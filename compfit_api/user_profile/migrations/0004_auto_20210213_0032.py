# Generated by Django 3.1.2 on 2021-02-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20210212_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutplaylist',
            name='date_created',
            field=models.DateField(),
        ),
    ]
