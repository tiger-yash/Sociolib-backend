# Generated by Django 3.2.6 on 2021-11-10 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_bookinfo_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='reviews',
            new_name='book_review',
        ),
    ]