from django.shortcuts import render,redirect
from django.contrib import messages
from urllib.parse import urlencode
from django.urls import reverse
from .models import Contact
# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        listing_id = request.POST['listing_id']
        listing_title = request.POST['listing_title']
        realtor_email = request.POST['realtor_email']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            if Contact.objects.filter(user_id=request.user.id, listing_id= listing_id).exists():
                messages.error(request,'You have already made an inquiry for this listing')
                # query_string =  urlencode({'listing_app:listing': listing_id})
                return redirect('/listing/'+listing_id)

        contact = Contact(listing=listing_title,listing_id=listing_id,name=name,
                                        email=email,message=message,user_id=user_id)
        contact.save()
        messages.error(request,'You request has been submitted, a realtor will get beck to you soon.')

    return redirect('/listing/'+listing_id)
