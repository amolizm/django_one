# Generated by Django 5.0.7 on 2024-07-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('japanese', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiragana',
            name='unicode',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='kanji',
            name='unicode',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='katakana',
            name='unicode',
            field=models.IntegerField(max_length=8),
        ),
    ]
