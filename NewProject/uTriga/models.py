from django.db import models
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
    
class Advertiser(models.Model):
    licence_ticket=models.CharField(max_length=255,null=True, blank=True)
    brand_name=models.CharField(max_length=255)
    num_of_posts=models.IntegerField(null=True, blank=True)
    user=models.OneToOneField(User)
    phone_number=models.CharField(max_length=255,null=True, blank=True)
    def __unicode__(self):
        return self.brand_name

class Category(models.Model):
   category_name= models.CharField(max_length=255)
   sub_category_ID=models.IntegerField(null=True, blank=True)
   category_user_number=models.IntegerField(null=True, blank=True)
   def __unicode__(self):
        return self.category_name


class Event(models.Model):
    event_name=models.CharField(max_length=255)
    event_date=models.DateField()
    event_time=models.TimeField()
    reminder_date=models.DateField()
    reminder_time=models.TimeField()
    created=models.DateField(auto_now_add=True)
    updated= models.DateField(auto_now=True)

    event_advertiser=models.ForeignKey(Advertiser)
    event_category = models.ManyToManyField('Category')
    
    venue=models.CharField(max_length=255)
    price=models.CharField(max_length=10)
    event_image=models.ImageField(upload_to='image_uploads/',
                                  null=True, blank=True)
    def __unicode__(self):
        return self.event_name

   
class AppUser(models.Model):
    mobile_num=models.IntegerField(max_length=10)
    username = models.CharField(max_length=60)
    email= models.EmailField()
    birth_date= models.DateField(null=True, blank=True)
    event = models.ManyToManyField("Event",null=True, blank=True)
    #news = models.ManyToManyField(blank=True,"News")
    def __unicode__(self):
        return str(self.mobile_num)

##class News(models.Model):
##    news_title=models.CharField()
##    created=models.DateField(auto_now_add=True)
##    updated= models.DateField(auto_now=True)
##
##    event_advertiser=models.ForeignKey(Advertiser)
##    event_category = models.ManyToManyField('Category')
##
##    def __unicode__(self):
##        return self.news_title
##
## 
