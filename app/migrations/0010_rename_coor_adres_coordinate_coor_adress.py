# Generated by Django 4.2.16 on 2024-09-30 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_coordinate_coor_to_pub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinate',
            old_name='coor_adres',
            new_name='coor_adress',
        ),
    ]
