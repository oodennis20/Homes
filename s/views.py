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
            home = Home.objects.get(pk=request.user.more.home_id.id)
            # posts = Posts.objects.filter(home=request.user.more.home_id.id)
            # businesses = Business.objects.filter(home=request.user.more.home_id.id)

            return render(request, 'homes/home.html', {"home": home})
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
def exitHome(request,homeId):

	if More.objects.filter(user_id = request.user).exists():
		More.objects.get(user_id = request.user).delete()
		messages.error(request, 'You have succesfully exited this Neighbourhood.')
		return redirect('home')

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

@login_required(login_url='/accounts/login/')
def add_comment(request,pk):
    image = get_object_or_404(Home, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.poster = current_user
            comment.save()

            return redirect('home')

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"user":current_user,"comment_form":form})

@login_required(login_url='/accounts/login/')
def more(request,homeId):

	neighbourhood = Home.objects.get(pk = homeId)
	if More.objects.filter(user_id = request.user).exists():

		More.objects.filter(user_id = request.user).update(home_id = neighbourhood)
	else:

		More(user_id=request.user,home_id = neighbourhood).save()

	# messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
	return redirect('home')


@login_required(login_url='/accounts/login/')
def create_house(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateHouseForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit = False)
            house.user = current_user
            house.save()
            messages.success(request, 'You Have succesfully created a hood.Now proceed and join a hood')
        return redirect('home')
    else:
        form = CreateHouseForm()
    return render(request,'houses/create_houses.html',{"form":form})

@login_required(login_url='/accounts/login/')
def delete_house(request,id):

	Home.objects.filter(user = request.user,pk=id).delete()
	messages.error(request,'Succesfully deleted the house you had posted')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/accounts/login/")
def logout_request(request):
    '''
    view function renders home page once logout
    '''
    logout(request)
    return redirect('home') 