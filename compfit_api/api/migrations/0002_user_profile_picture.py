# Generated by Django 3.1.2 on 2021-02-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]