# Generated by Django 4.2 on 2023-05-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicle_outdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='outdate',
            field=models.DateField(null=True),
        ),
    ]
