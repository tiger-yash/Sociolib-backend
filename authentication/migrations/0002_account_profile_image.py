# Generated by Django 3.2.6 on 2021-10-29 11:53

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default=authentication.models.get_default_profile_image, max_length=255, null=True, upload_to=authentication.models.get_profile_image_filepath),
        ),
    ]
