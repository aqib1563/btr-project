from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from .models import Listing
from listing_app.choices import state_choices,bedroom_choices,price_choices
# Create your views here.
def listings_page(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 6) # Show 25 contacts per page

    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    template_name = 'listing_app/listings.html'
    context = {'listings':paged_listing}
    return render(request,template_name,context)

def listing_page(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {'listing':listing}
    template_name = 'listing_app/listing.html'
    return render(request,template_name,context)

def search(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:6]
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            listings = Listing.objects.filter(description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            listings = Listing.objects.filter(city__iexact=city)
    # State
    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            listings = Listing.objects.filter(state__iexact=state)
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            listings = Listing.objects.filter(bedrooms=bedrooms)
    # price
    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            listings = Listing.objects.filter(price=price)


    context = {
                'listings':listings,
                'state_choices':state_choices,
                'bedroom_choices':bedroom_choices,
                'price_choices':price_choices,
                'values':request.GET
    }
    template_name = 'listing_app/search.html'
    return render(request,template_name,context)
