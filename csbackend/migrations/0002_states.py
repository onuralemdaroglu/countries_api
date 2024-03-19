# Generated by Django 5.0.3 on 2024-03-19 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csbackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=60)),
                ('countryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csbackend.countries')),
            ],
        ),
    ]