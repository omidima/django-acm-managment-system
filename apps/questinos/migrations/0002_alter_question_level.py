# Generated by Django 4.2 on 2023-05-07 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questinos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.IntegerField(choices=[(0, 'low'), (1, 'middle'), (2, 'high')], default=0, max_length=1, verbose_name='level'),
        ),
    ]
