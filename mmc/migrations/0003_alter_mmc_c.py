# Generated by Django 4.2.6 on 2023-10-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmc', '0002_mmc_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmc',
            name='c',
            field=models.IntegerField(),
        ),
    ]
