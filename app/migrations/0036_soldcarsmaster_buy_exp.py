# Generated by Django 3.2.4 on 2021-06-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_soldcarsmaster_total_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldcarsmaster',
            name='Buy_EXP',
            field=models.CharField(default='NULL', max_length=20, null=True),
        ),
    ]