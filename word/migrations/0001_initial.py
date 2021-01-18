# Generated by Django 3.1.5 on 2021-01-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordsDefining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('pegi', models.PositiveIntegerField()),
                ('commentCount', models.PositiveBigIntegerField()),
                ('downloads', models.PositiveBigIntegerField()),
                ('ranking', models.PositiveIntegerField()),
            ],
        ),
    ]