# Generated by Django 3.1.3 on 2020-11-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0008_auto_20201112_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]