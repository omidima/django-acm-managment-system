# Generated by Django 4.2 on 2023-05-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questinos', '0003_answer_created_at_answeratemp_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='file_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
