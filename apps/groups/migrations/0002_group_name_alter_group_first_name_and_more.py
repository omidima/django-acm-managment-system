# Generated by Django 4.2 on 2023-05-06 18:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='group',
            name='first_name',
            field=models.CharField(blank=True, default=1, max_length=150, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_name',
            field=models.CharField(blank=True, default=1, max_length=150, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^(09)[0-9]{9}$')], verbose_name='phone number'),
        ),
    ]