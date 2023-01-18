from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Rental,Address, LocalAddress

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'terrain'})},
    }







admin.site.register(Rental, RentalAdmin)
admin.site.register(Address, RentalAdmin)
admin.site.register(LocalAddress, MapAdmin)


