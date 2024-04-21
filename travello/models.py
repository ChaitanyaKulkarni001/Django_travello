from django.db import models

# Create your models here.

class Destination(models.Model):
    # id : int // as database will have own id
    name = models.CharField(max_length=100)  #str
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()# str
    price= models.IntegerField()
    offer= models.BooleanField(default=False)