# Generated by Django 3.2.4 on 2021-06-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_expencemaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadmaster',
            name='OfferPrice',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]
