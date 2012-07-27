# Create your views here.
"""
Code that should be copy and pasted in to
reg/views.py to as a skeleton for creating
the authentication views
"""
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

@csrf_exempt
def do_login(request):
    form = LoginForm()# create an instance of a login form
    logged_in =request.user.is_authenticated() # get login status
    
    if logged_in:
        render_to_response('reg/login.html',locals())# return  
    if request.method == 'POST':
        
        #YOUR CODE HERE
        usr=request.POST['username'] #get username
        passwrd=request.POST['password']# get password
        form=LoginForm(request.POST) # create instance of loginform
        user=authenticate(username=usr,password=passwrd)# authenticate user
        if user is not None:
            if user.is_active:
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
    return render_to_response('reg/logout.html')
