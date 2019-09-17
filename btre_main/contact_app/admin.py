from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['listing','listing_id','name','email','phone','message','contact_date']
    list_display_links = ['listing_id','name']
    search_fields = ['listing','name','email']
    list_per_page = 25

admin.site.register(Contact,ContactAdmin)
