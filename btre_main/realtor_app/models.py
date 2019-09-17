from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.TextField()
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='photos/realtor/%Y/%m/%d')
    hire_date = models.DateTimeField(default=datetime.now())
    is_mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.name
