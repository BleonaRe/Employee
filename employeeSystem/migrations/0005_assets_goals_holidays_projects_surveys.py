# Generated by Django 5.1.4 on 2025-03-22 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeSystem', '0004_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=200)),
                ('asset_type', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('condition', models.CharField(choices=[('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeSystem.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('target_date', models.DateField()),
                ('achieved', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeSystem.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_name', models.CharField(max_length=200)),
                ('holiday_date', models.DateField()),
                ('is_approved', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeSystem.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeSystem.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_title', models.CharField(max_length=200)),
                ('survey_date', models.DateField()),
                ('feedback', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeSystem.employee')),
            ],
        ),
    ]
