# Generated by Django 4.1 on 2022-08-23 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='phone_number',
            new_name='phonenumber',
        ),
    ]
