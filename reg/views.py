from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from uTriga.forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from uTriga.models import Advertiser

@csrf_exempt
def do_login(request):
    form = LoginForm()# create an instance of a login form
    logged_in =request.user.is_authenticated() # get login status
    
    if logged_in:
        message='You are logged in '
        return render_to_response('reg/login.html',locals())# return  
    if request.method == 'POST':
        usr=request.POST['username'] #get username
        passwrd=request.POST['password']# get password
        form=LoginForm(request.POST) # create instance of loginform
        user=authenticate(username=usr,password=passwrd)# authenticate user
        if user is not None:
            if user.is_active:]
                login(request,user) #log user in
                return HttpResponseRedirect("/utriga/post/")

            else:
                pass
    else:
        pass
    
    
    return render_to_response('reg/login.html',locals())


@csrf_exempt
def do_logout(request):
    logout(request) #log user out
    return render_to_response('reg/logout.html',locals())



@csrf_exempt
def sign_up(request):
    signed_up=False
    form=SignUpForm()# create instance of a sign up form
    logged_in =request.user.is_authenticated()

    if logged_in:
        return render_to_response('reg/logoutSignUp.html',locals())# return

    if request.method == 'POST':
        new_user = User.objects.create_user(
            request.POST['username'],
            request.POST['email'],
            request.POST['password'])
        new_user.is_active = True
        new_user.save()
##      new_user.first_name = first_name
##      new_user.last_name = last_name
        
##        adv=Advertiser.objects.create
        new_advertiser=Advertiser(user=new_user,
                           licence_ticket=request.POST['licence_ticket'],
                           brand_name=request.POST['brand_name'],
                           phone_number=request.POST['phone_number'],
                           num_of_posts=0
                           )

        new_advertiser.save()
        signed_up=True
        render_to_response('reg/sign_up.html',locals())
        
    return render_to_response('reg/sign_up.html',locals())
    
   
