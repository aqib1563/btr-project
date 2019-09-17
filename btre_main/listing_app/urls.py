from django.urls import path
from . import views

app_name = 'listing_app'
urlpatterns = [
    path('listings/',views.listings_page,name='listings'),
    path('<int:listing_id>',views.listing_page,name='listing'),
    path('search/',views.search,name='search'),
]
