# Generated by Django 4.1.5 on 2023-01-17 17:01

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('aysaApp', '0004_localaddress_lat_localaddress_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='localaddress',
            name='address',
            field=mapbox_location_field.models.AddressAutoHiddenField(default=1, map_id='map'),
            preserve_default=False,
        ),
    ]