# Generated by Django 3.2.4 on 2021-06-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_inventorymaster_mfg'),
    ]

    operations = [
        migrations.AddField(
            model_name='expencemaster',
            name='CarRegNo',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]
