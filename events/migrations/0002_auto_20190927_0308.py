# Generated by Django 2.2.5 on 2019-09-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='updated',
            new_name='modified',
        ),
        migrations.AddField(
            model_name='event',
            name='score',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]