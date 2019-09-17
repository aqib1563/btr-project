from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now,blank=True)
    user_id = models.EmailField(blank=True)

    def __str__(self):
        return self.name
