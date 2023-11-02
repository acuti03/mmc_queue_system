# Generated by Django 4.2.6 on 2023-10-26 21:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmc', '0005_mmc_p_0_mmc_p_k_mmc_k_mmc_mu_k_mmc_rho_alter_mmc_c_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmc',
            name='P_0',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mmc',
            name='P_k',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None),
        ),
        migrations.AlterField(
            model_name='mmc',
            name='c',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mmc',
            name='k',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
        migrations.AlterField(
            model_name='mmc',
            name='mu',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mmc',
            name='mu_k',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None),
        ),
        migrations.AlterField(
            model_name='mmc',
            name='myLambda',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mmc',
            name='rho',
            field=models.FloatField(),
        ),
    ]