# Generated by Django 3.2.4 on 2021-06-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_soldcarsmaster_currentcust'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldcarsmaster',
            name='Amount',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]