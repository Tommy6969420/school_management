# Generated by Django 4.2.6 on 2023-12-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_alter_billing_previous_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billing',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
