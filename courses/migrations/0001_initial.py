# Generated by Django 5.2 on 2025-04-09 09:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(choices=[('A0001', 'A0001'), ('B0002', 'B002'), ('C0003', 'C003'), ('D0004', 'D004'), ('E0005', 'E0005')], max_length=200)),
                ('course_code', models.CharField(choices=[('0001', '0001'), ('0002', '0002'), ('0003', '0003'), ('0004', '0004'), ('0005', '0005')], max_length=20)),
                ('medium', models.CharField(max_length=50)),
                ('admission_criteria', models.TextField(blank=True, null=True)),
                ('fee', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('parental_care', models.BooleanField()),
                ('location', models.CharField(choices=[('INDOOR', 'Indoor'), ('OUTDOOR', 'Outdoor')], default='INDOOR', max_length=20)),
                ('class_size', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tutors.tutor')),
            ],
        ),
    ]
