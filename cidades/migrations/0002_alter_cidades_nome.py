# Generated by Django 5.0.6 on 2024-06-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidades',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]