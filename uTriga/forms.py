from django import forms
from models import Event,Advertiser                                     
from django.db import models
#from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget


def make_custom_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%Y-%m-%d'
        formfield.widget.attrs.update({'class':'datepicker', 'readonly':'true'})
    
    if isinstance(f,models.TimeField):
        formfield.widget.format='%H:%M:%S'
        formfield.widget.attrs.update({'class':'timepicker', 'readonly':'true'})

    return formfield

class EventForm(forms.ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model=Event
        exclude=['reminder_date','event_advertiser','reminder_time']
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class SignUpForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    licence_ticket=forms.CharField()
    email=forms.EmailField()
    phone_number=forms.CharField()
    brand_name=forms.CharField()
    
class ContactForm(forms.Form):
    full_name=forms.CharField()
    email=forms.EmailField()
    telephone=forms.CharField()
    message= forms.CharField(widget=forms.Textarea)



##class AdvSignUpForm(forms.Form):
##    class Meta:
##        model=Advertiser
##
##def validate_phone_number(value):
##    if value % 2 != 0:
##        raise ValidationError(u'%s is not an even number' % value)
##
##
##
##def handle_uploaded_file(f):
##    destination = open('image_uploads/X.jpg', 'wb+')
##    destination.write(str(f))
##    destination.close()
