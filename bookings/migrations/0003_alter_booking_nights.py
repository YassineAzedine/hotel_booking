# Generated by Django 5.2 on 2025-05-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_booking_nights_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='nights',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
