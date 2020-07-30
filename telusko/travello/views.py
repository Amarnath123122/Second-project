from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False


    dest2 = Destination()
    dest2.name = 'kedar'
    dest2.desc = 'The City That is for shiva'
    dest2.img = 'destination_2.jpg'
    dest2.price = 70060
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'badari'
    dest3.desc = 'The City That worships lord vishnu'
    dest3.img = 'destination_3.jpg'
    dest3.price = 7000
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests': dests})
	