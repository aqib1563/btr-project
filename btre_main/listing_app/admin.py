from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ['id','title','city','zip_code','price','state','bedrooms','is_published',]
    list_display_links = ['id','title']
    list_editable = ['is_published']
    search_fields = ['title','city','price','zip_code']
    list_per_page = 25
admin.site.register(Listing,ListingAdmin)
