# Generated by Django 5.0.7 on 2024-07-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('japanese', '0002_alter_hiragana_unicode_alter_kanji_unicode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiragana',
            name='unicode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='kanji',
            name='unicode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='katakana',
            name='unicode',
            field=models.IntegerField(),
        ),
    ]
