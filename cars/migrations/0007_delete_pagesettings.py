# Generated by Django 4.2.13 on 2024-06-02 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_image_cover_alter_car_owner_pagesettings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageSettings',
        ),
    ]