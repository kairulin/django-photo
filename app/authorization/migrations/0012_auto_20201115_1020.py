# Generated by Django 3.1.3 on 2020-11-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0011_auto_20201115_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photomessage',
            name='message_post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
