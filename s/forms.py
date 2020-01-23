from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateHouseForm(forms.ModelForm):

	class Meta:
		model = Home
		exclude = ['user']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email', 'u_home']

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        exclude =['poster','image']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,10)]

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Posts
#         fields = ['title', 'content']