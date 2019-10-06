# Generated by Django 2.2.6 on 2019-10-06 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postalcode', '0003_auto_20191006_0604'),
        ('events', '0008_auto_20191006_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='postalCode',
            field=models.ForeignKey(default=45200, on_delete=django.db.models.deletion.CASCADE, to='postalcode.PostalCode'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='username_id', to=settings.AUTH_USER_MODEL, to_field='username'),
            preserve_default=False,
        ),
    ]