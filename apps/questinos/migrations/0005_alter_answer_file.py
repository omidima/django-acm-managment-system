# Generated by Django 4.2 on 2023-05-08 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questinos', '0004_answer_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='file',
            field=models.FileField(upload_to='uploads', verbose_name='file'),
        ),
    ]
