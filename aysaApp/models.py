import geocoder

from django.db import models
from django_google_maps import fields as map_fields
from mapbox_location_field.models import LocationField, AddressAutoHiddenField
# Create your models here.
from aysa.settings import MAPBOX_KEY


class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)


class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=MAPBOX_KEY)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args,**kwargs)

class LocalAddress(models.Model):
    location = LocationField()
    address = AddressAutoHiddenField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=MAPBOX_KEY)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(LocalAddress, self).save(*args,**kwargs)
