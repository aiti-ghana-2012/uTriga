from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from models import Advertiser,Category,User,Event
from django import forms
from forms import EventForm,ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.contrib.auth.views import password_reset

def home(request):

    html="<html><center><b><h1>WELCOME TO uTriga</h1></b></center></html>"
    return render_to_response("base.html",locals()) 
            
@csrf_exempt
def post_advert(request):
    logged_in =request.user.is_authenticated() # get login status
    if logged_in:
        form=EventForm()
        current_user=request.user
        this_advertiser= Advertiser.objects.get(user=current_user)
        if request.method == 'POST': # if user clicks submit button do...
            event_instance= Event(event_advertiser=this_advertiser,
                                  reminder_date=request.POST['event_date'],
                                  reminder_time=request.POST['event_time'])
            form=EventForm(request.POST,request.FILES,instance=event_instance)# get form field inputs
            
            if form.is_valid():
                form.save() # save in database
                return render_to_response("post_done.html",locals())
        else:
            return render_to_response("post_advert.html",locals())
    else:
        return HttpResponseRedirect('/utriga/reg/login/')
    
    return render_to_response("post_advert.html",locals())


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

# uploads a players match
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        #scoreone = int(request.POST['scoreone'])
        #scoretwo = int(request.POST['scoretwo'])
        #m = Match.objects.create()
        #MatchParticipant.objects.create(player = Player.objects.get(pk=1), match = m, score = scoreone)
        #MatchParticipant.objects.create(player = Player.objects.get(pk=2), match = m, score = scoretwo)

        user_name=request.POST['username']
        phone_number=request.POST['mobile']
        e_mail=request.POST['email']
        #birth_day=request.POST['birth_day']
        #event=request.POST['event']
        thisAppUser= AppUser(mobile_num=phone_number,username=user_name, email=e_mail)

        thisAppUser.save()

    return HttpResponse("Match uploaded" )


@csrf_exempt
def contact_us(request):
    form=ContactForm()
    return render_to_response("contact_us.html",locals())
    #return HttpResponse('ABOUT US')


def boot_test(request):
    return render_to_response("boot_test.html",locals())

def user_list(request):
    logged_in =request.user.is_authenticated() # get login status
    list_of_users= User.objects.all()# get all users

    return render_to_response("users.html",locals())
    #return HttpResponse('user list')

def ad_list(request):
    logged_in =request.user.is_authenticated() # get login status
    list_of_ads= Event.objects.all() # get all events

    return render_to_response("ads.html",locals())
    #return HttpResponse('ad list')

def advertiser_list(request):
    logged_in =request.user.is_authenticated() # get login status
    list_of_advertisers= Advertiser.objects.all() # get all events

    return render_to_response("advertisers.html",locals())
    #return HttpResponse('advertiser list')

def reset_password(request):
    
    template_name="reset_password.html"

    return password_reset(request)
    #return HttpResponse('Reset')

