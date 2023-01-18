from django.shortcuts import render
from django.http import HttpResponse

from aysa.settings import MAPBOX_KEY
from .models import Rental,Address,LocalAddress

# Create your views here.

def index(request):
    mapbox_access_token = MAPBOX_KEY
    rental = Rental.objects.all()
    adress = Address.objects.all()
    newaddress = LocalAddress.objects.all()
    return render(request, 'aysa/index.html',
                  { 'mapbox_access_token': mapbox_access_token, 'rental': rental,'adress':adress, 'newaddress':newaddress })