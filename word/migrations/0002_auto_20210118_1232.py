# Generated by Django 3.1.5 on 2021-01-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordsdefining',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='wordsdefining',
            name='commentCount',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='wordsdefining',
            name='downloads',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='wordsdefining',
            name='pegi',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='wordsdefining',
            name='ranking',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='wordsdefining',
            name='word',
            field=models.CharField(max_length=30),
        ),
    ]
