
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from egyon import settings
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from django.template.defaultfilters import truncatechars



class Vendor(models.Model):
    Name = models.CharField(max_length=250, blank=True, unique=True,null = True)
    vendor_slug = models.SlugField(unique=True, db_index=True)
    address = models.CharField(max_length=250, blank=True,null = True,)
    Longitude = models.FloatField(default=0,null=True, blank= True)
    Latitude = models.FloatField(default=0,null=True, blank= True)
    delivery_fees = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.Name)
    class Meta:
        verbose_name_plural = "Vendors"


 


class Category(models.Model):
    Category_name = models.CharField(max_length=250,unique = True,)
    display_name =  models.CharField(max_length=250, blank=True,null = True)
    categoryslug = models.SlugField(unique=True, db_index=True,blank=True,null = True)
    image = models.ImageField(
        upload_to="Categories", blank=True,null = True )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    Vendor = models.ManyToManyField(
        Vendor, blank=True,)

    
    
    def __str__(self):
        return str(self.Category_name)
        
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url_category(self):
        return reverse('categories_and_products:category_details', args=[self.Restaurant.restaurant_slug] + [self.categoryslug])

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=250, blank=True)
    ArabicName = models.CharField(max_length = 250, blank = True, null= True)
    productslug = models.SlugField(unique=True, db_index=True,)
    Vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, blank=True,null= True)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null = True,)
    boughtPrice = models.FloatField(blank=True, null=True, default=0)
    offerPercentage = models.FloatField(blank=True, null=True,)
    active = models.BooleanField(default=True)
    Most_Popular = models.BooleanField(default=False)
    New_Products = models.BooleanField(default=False)
    Best_Offer = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    limit = models.IntegerField(default= 0, blank = True, null = True)

    def __str__(self):
        arabic_string = self.ArabicName
        arabic_string.encode('unicode-escape')
        return arabic_string
    

