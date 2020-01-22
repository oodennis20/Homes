from django.shortcuts import render
from rest_framework import viewsets
from s import models
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if More.objects.filter(user_id=request.user).exists():
            home = Home.objects.get(pk=request.user.join.hood_id.id)
            posts = Posts.objects.filter(home=request.user.join.hood_id.id)
            businesses = Business.objects.filter(home=request.user.join.hood_id.id)

            return render(request, 'homes/home.html', {"home": home, "businesses": businesses, "posts": posts})
        else:
            neighbourhoods = Home.objects.all()
            return render(request, 'index.html',{"neighbourhoods":neighbourhoods})
    else:
        neighbourhoods = Home.objects.all()
        return render(request, 'index.html',{"neighbourhoods":neighbourhoods})

@login_required(login_url='/accounts/login')
def profile(request):

    profile = Profile.objects.get(user = request.user)
    return render(request,'profiles/profile.html',{"profile":profile,"homes":homes}) 

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    profile = Profile.objects.get(user = request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES,instance = profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.email = current_user.email
            profile.save()
        return redirect('profile')

    else:
        form = EditProfileForm(instance = profile)
    return render(request, 'profiles/edit_profile.html', {"form": form})


def homes(request):

	homes = Home.objects.filter(user = request.user)
	return render(request,'homes/home.html',{"homes":homes})


@login_required(login_url="/accounts/login/")
def logout_request(request):
    '''
    view function renders home page once logout
    '''
    logout(request)
    return redirect('home') 