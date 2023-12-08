# Generated by Django 4.2.6 on 2023-12-08 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrative', '0003_class_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='class',
            name='section',
            field=models.CharField(choices=[('Rose', 'Rose'), ('Lotus', 'Lotus'), ('Marigold', 'Marigold'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=64),
        ),
    ]