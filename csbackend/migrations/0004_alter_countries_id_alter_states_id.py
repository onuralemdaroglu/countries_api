# Generated by Django 5.0.3 on 2024-03-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csbackend', '0003_alter_states_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='states',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
