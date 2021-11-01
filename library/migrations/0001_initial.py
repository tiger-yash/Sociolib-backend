# Generated by Django 3.2.6 on 2021-11-01 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('genre', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('cover_image', models.ImageField(blank=True, default=library.models.get_default_cover_image, max_length=255, null=True, upload_to=library.models.get_cover_image_filepath)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=280)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('is_owned', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_book', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='critic', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
