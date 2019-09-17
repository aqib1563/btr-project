from django.shortcuts import render
from listing_app.models import Listing
from listing_app.models import Realtor
from listing_app.choices import state_choices,bedroom_choices,price_choices
# Create your views here.

def home_page(request):
    listings = Listing.objects.all()
    context = {
                'listings':listings,
                'state_choices':state_choices,
                'bedroom_choices':bedroom_choices,
                'price_choices':price_choices
            }
    template_name = 'page_app/index.html'
    return render(request,template_name,context)

def about_page(request):
    realtors = Realtor.objects.all()
    is_mvp = Realtor.objects.all().filter(is_mvp=True)
    context = {'realtors':realtors,
                'is_mvp':is_mvp
            }
    template_name = 'page_app/about.html'
    return render(request,template_name,context)
