# Generated by Django 4.1.6 on 2023-02-02 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_user_ticket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='ticket',
            name='size',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_booked',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ticket_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(default='No description'),
        ),
    ]
