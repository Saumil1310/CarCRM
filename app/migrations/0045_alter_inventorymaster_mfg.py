# Generated by Django 3.2.4 on 2021-06-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20210625_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymaster',
            name='Mfg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
