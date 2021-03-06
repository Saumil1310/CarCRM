# Generated by Django 3.2.4 on 2021-06-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_auto_20210625_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermaster',
            name='Amount',
            field=models.IntegerField(default='NULL', max_length=255),
        ),
        migrations.AlterField(
            model_name='customermaster',
            name='OfferPrice',
            field=models.IntegerField(default='NULL', max_length=255),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='BodyShop_Amount',
            field=models.IntegerField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='BuyPrice',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='FinalPrice',
            field=models.IntegerField(default='00', max_length=255),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='Fuel_Amount',
            field=models.IntegerField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='MOT_Amount',
            field=models.IntegerField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='Mechanic_Amount',
            field=models.IntegerField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='Mfg',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='Milage',
            field=models.IntegerField(default='KW01', max_length=255),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='SellPrice',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='Total_Expenses',
            field=models.IntegerField(default='NULL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='Travelling_Amount',
            field=models.IntegerField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='leadgermaster',
            name='Amount',
            field=models.IntegerField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='leadgermaster',
            name='FinalPrice',
            field=models.IntegerField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='leadmaster',
            name='OfferPrice',
            field=models.IntegerField(default='NULL', max_length=255),
        ),
        migrations.AlterField(
            model_name='soldcarsmaster',
            name='Amount',
            field=models.IntegerField(default='NULL', max_length=255),
        ),
        migrations.AlterField(
            model_name='soldcarsmaster',
            name='BuyPrice',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='soldcarsmaster',
            name='Buy_EXP',
            field=models.IntegerField(default='NULL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='soldcarsmaster',
            name='Milage',
            field=models.IntegerField(default='KW01', max_length=255),
        ),
        migrations.AlterField(
            model_name='soldcarsmaster',
            name='Profit',
            field=models.IntegerField(default='NULL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='soldcarsmaster',
            name='SellPrice',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='soldcarsmaster',
            name='Total_Expenses',
            field=models.IntegerField(default='NULL', max_length=20, null=True),
        ),
    ]
