# Generated by Django 5.1.3 on 2024-11-19 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
                ('Type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='usertable',
            name='LOGIN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Disaster_management_app.logintable'),
        ),
    ]
