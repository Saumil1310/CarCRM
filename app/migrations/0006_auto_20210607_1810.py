# Generated by Django 3.2.4 on 2021-06-07 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210607_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leadmaster',
            old_name='Choice1',
            new_name='Choices',
        ),
        migrations.RemoveField(
            model_name='leadmaster',
            name='Choice2',
        ),
        migrations.RemoveField(
            model_name='leadmaster',
            name='Choice3',
        ),
        migrations.RemoveField(
            model_name='leadmaster',
            name='Choice4',
        ),
        migrations.RemoveField(
            model_name='leadmaster',
            name='Choice5',
        ),
        migrations.RemoveField(
            model_name='leadmaster',
            name='Choice6',
        ),
    ]
