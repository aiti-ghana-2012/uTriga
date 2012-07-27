from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from models import Event,Advertiser,Category,User,News
from django import forms
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.db import models
from django.forms.extras.widgets import SelectDateWidget
def home(request):

    html="<html><center><b><h1>WELCOME TO uTriga</h1></b></center></html>"
    return render_to_response("index.html",locals()) 

def make_custom_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%m/%d/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield

class EventForm(forms.ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model=Event
        #event_date=models.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
        #exclude=['reminder_date','event_advertiser',]

def post_advert(request):
    logged_in =request.user.is_authenticated() # get login status
    if logged_in:    
        form=EventForm()
        #return HttpResponse('In post_advert')
        return render_to_response("post_advert.html",locals())

    return HttpResponseRedirect('/utriga/reg/login/')



def see_posts(request): 
    #return HttpResponse('In see posts')
    return render_to_response("see_posts.html",locals())

def services(request):
    return render_to_response("services.html",locals())
    #return HttpResponse('OUR SERVICES')


def projects(request):
    
    return render_to_response("projects.html",locals())
    #return HttpResponse('OUR PRODUCTS')

def about_us(request):
    return render_to_response("about_us.html",locals())
    #return HttpResponse('ABOUT US')

def contact_us(request):
    return render_to_response("contact_us.html",locals())
    #return HttpResponse('ABOUT US')


def boot_test(request):
    return render_to_response("boot_test.html",locals())
