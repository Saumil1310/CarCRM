# Generated by Django 3.2.4 on 2021-06-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_customermaster_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermaster',
            name='Comment',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AddField(
            model_name='customermaster',
            name='OfferPrice',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AddField(
            model_name='customermaster',
            name='Payment',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]
