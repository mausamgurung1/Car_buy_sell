from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from app.forms import LocationForm

from .forms import ListingForm
from .models import Listing


# Create your views here.
def main_view(request):
    return render(request, "views/main.html", {"name": "AutoMax"})


@login_required
def home_view(request):
    listings = Listing.objects.all()
    
    
    
    context = {
        'listings': listings
    }
    return render(request, "views/home.html", context)


@login_required
def list_view(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        listing_form:ListingForm()
        location_form:LocationForm()


    return render(request, 'views/list.html', {'listing_form': ListingForm, 'Location_form': LocationForm})