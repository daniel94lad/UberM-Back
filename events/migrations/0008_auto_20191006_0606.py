# Generated by Django 2.2.6 on 2019-10-06 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_eventassistance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='postalCode',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
    ]