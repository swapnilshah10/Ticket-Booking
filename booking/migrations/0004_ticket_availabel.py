# Generated by Django 4.1.6 on 2023-02-02 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_ticket_date_created_ticket_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='availabel',
            field=models.IntegerField(default=100),
        ),
    ]