from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.forms import URLField

# Create your models here.

# the profile model
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic=CloudinaryField('image')
    username =models.CharField(max_length=100 , null=True)
    bio=models.TextField(null=True)
    contacts=models.CharField(max_length=300)