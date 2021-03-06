# Generated by Django 3.2.4 on 2021-06-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_alter_leadmaster_leademail'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorymaster',
            name='BodyShop_Amount',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='BodyShop_Details',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='Fuel_Amount',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='Fuel_Details',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='MOT_Amount',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='MOT_Details',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='Mechanic_Amount',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='Mechanic_Details',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='Total_Expenses',
            field=models.CharField(default='NULL', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='Travelling_Amount',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='inventorymaster',
            name='Travelling_Details',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]
