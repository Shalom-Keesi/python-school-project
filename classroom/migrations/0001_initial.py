# Generated by Django 5.0.7 on 2024-07-14 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('school_year', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('room_number', models.IntegerField()),
                ('specialty', models.TextField(blank=True, null=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classes', to='teacher.teacher')),
            ],
        ),
    ]
