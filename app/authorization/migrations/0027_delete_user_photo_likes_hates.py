# Generated by Django 3.1.3 on 2020-11-21 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0026_auto_20201121_0715'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_photo_likes_hates',
        ),
    ]