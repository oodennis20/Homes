from django.db import models  
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Home(models.Model):
    home_photo = ImageField(blank=True,manual_crop='')
    home_description = models.TextField(max_length=200, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    @classmethod
    def get_hoods(cls):
        hoods = Home.objects.all()

        return hoods

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo = ImageField(blank=True,manual_crop='')
    bio= models.CharField(max_length=240, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    

    @receiver(post_save, sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender,instance, **kwargs):
        instance.profile.save()
    
    
    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

class More(models.Model):
	user_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True )
	hood_id = models.ForeignKey(Home, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.user_id