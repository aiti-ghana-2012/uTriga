from django.db import models
from django.core.exceptions import ValidationError

    
class Advertiser(models.Model):
    advertiser_name=models.CharField(max_length=60)
    advertiser_email=models.EmailField()
    num_of_posts=models.IntegerField()
    def __unicode__(self):
        return self.advertiser_name

class Category(models.Model):
   category_name= models.CharField(max_length=30)
   sub_category_ID=models.IntegerField()
   category_user_number=models.IntegerField()
   def __unicode__(self):
        return self.category_name


class Event(models.Model):
    event_name=models.CharField(max_length=60)
    event_image=models.ImageField(upload_to='image_uploads/',
                                  null=True, blank=True)
    event_date=models.DateField()
    reminder_date=models.DateField()
    created=models.DateField(auto_now_add=True)
    updated= models.DateField(auto_now=True)

    event_advertiser=models.ForeignKey(Advertiser)
    event_category = models.ManyToManyField('Category')

    venue=models.CharField(max_length=255)
    price=models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.event_name

class News(models.Model):
    news_title=models.CharField(max_length=255)
    created=models.DateField(auto_now_add=True)
    updated= models.DateField(auto_now=True)

    event_advertiser=models.ForeignKey(Advertiser)
    event_category = models.ManyToManyField('Category')

    def __unicode__(self):
        return self.news_title

    
class User(models.Model):
    username = models.CharField(max_length=60)
    email= models.EmailField()
    mobile_num=models.IntegerField(max_length=10)
    event = models.ManyToManyField("Event")
    news = models.ManyToManyField("News")
    def __unicode__(self):
        return self.username
