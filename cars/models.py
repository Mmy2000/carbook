from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify 
from django.db.models import Avg , Count
# Create your models here.

class Car(models.Model):
    owner = models.ForeignKey(User, related_name='car_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , help_text="enter your vin number her")
    image_cover = models.ImageField(upload_to='cars/')
    total_price = models.IntegerField(default=0)
    price_per_month = models.IntegerField(default=0,null=True,blank=True)
    description = models.TextField(max_length=10000)
    features = models.TextField(max_length=10000,null=True,blank=True)
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField(null=True,blank=True,unique=True)
    model = models.ForeignKey("Model",related_name='car_model', on_delete=models.CASCADE)
    mileage = models.CharField( max_length=50)
    transmission = models.CharField( max_length=50,null=True,blank=True)
    specifications = models.CharField( max_length=50,null=True,blank=True)
    fuel = models.CharField( max_length=50)
    color = models.CharField( max_length=50)
    cylinders = models.IntegerField()
    doors = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cars"


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Car,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("car_details", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

class CarImages(models.Model):
    car = models.ForeignKey(Car,related_name='Car_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='carimages/')


    class Meta:
        verbose_name_plural = "Car Images"

    def __str__(self):
        return str(self.car)


class Model(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Car Model"

    def __str__(self):
        return str(self.name)


    

    