# Generated by Django 4.2.6 on 2023-12-07 13:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=64)),
                ('section', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subj_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=64)),
                ('roll_no', models.IntegerField(default=0)),
                ('D_O_B', models.DateField()),
                ('admission_date', models.DateField(default=django.utils.timezone.now)),
                ('parents_name', models.CharField(max_length=64)),
                ('contact', models.CharField(max_length=14)),
                ('std_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrative.class')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='subject',
            field=models.ManyToManyField(to='administrative.subject'),
        ),
    ]
