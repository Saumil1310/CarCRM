# Generated by Django 3.2.4 on 2021-06-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20210622_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermaster',
            name='CustAddress',
            field=models.CharField(blank=True, default='NULL', max_length=255, null=True),
        ),
    ]
