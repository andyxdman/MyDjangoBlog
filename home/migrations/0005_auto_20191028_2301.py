# Generated by Django 2.2.5 on 2019-10-28 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191028_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='add_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateField(auto_now=True),
        ),
    ]
