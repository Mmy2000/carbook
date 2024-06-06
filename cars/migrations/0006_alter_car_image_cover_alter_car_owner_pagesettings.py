# Generated by Django 4.2.13 on 2024-06-02 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0005_rename_color_car_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image_cover',
            field=models.ImageField(upload_to='cars/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PageSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_cover', models.ImageField(upload_to='cars/')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_image', to='cars.car')),
            ],
        ),
    ]