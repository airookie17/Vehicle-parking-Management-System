# Generated by Django 3.1.3 on 2023-04-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='slotID',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]