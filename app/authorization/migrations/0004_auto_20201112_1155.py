# Generated by Django 3.1.3 on 2020-11-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_auto_20201112_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemphoto',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
