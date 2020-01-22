from django.db import models    
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Hood(models.Model):
    hood_photo = ImageField(blank=True,manual_crop='')
    hood_name = models.CharField(max_length=100, null=True)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_hoods(cls):
        hoods = Hood.objects.all()

        return hoods