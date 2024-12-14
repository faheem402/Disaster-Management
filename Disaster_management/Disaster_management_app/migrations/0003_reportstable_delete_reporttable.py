# Generated by Django 5.1.3 on 2024-11-20 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster_management_app', '0002_logintable_usertable_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Report', models.CharField(blank=True, max_length=150, null=True)),
                ('VOLUNTEER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disaster_management_app.volunteerstable')),
            ],
        ),
        migrations.DeleteModel(
            name='ReportTable',
        ),
    ]
