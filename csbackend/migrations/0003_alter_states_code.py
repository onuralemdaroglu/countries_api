# Generated by Django 5.0.3 on 2024-03-19 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csbackend', '0002_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='code',
            field=models.CharField(max_length=3),
        ),
    ]
