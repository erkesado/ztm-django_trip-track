# Generated by Django 4.2.9 on 2024-01-06 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='country_code',
            new_name='country',
        ),
    ]