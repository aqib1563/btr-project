from django.db import models
from datetime import datetime
from realtor_app.models import Realtor

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    description = models.TextField()
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathroome = models.DecimalField(max_digits=2, decimal_places=1)
    sqft = models.IntegerField()
    lot_size = models.FloatField()
    garage = models.IntegerField(default=0)
    list_date = models.DateTimeField(default=datetime.now())
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
