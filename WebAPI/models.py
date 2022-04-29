from django.db import models
from datetime import datetime
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.contrib import admin
from imagekit.admin import AdminThumbnail


class PhotoMedia(models.Model):
    imageurl = ProcessedImageField(upload_to='images/',
                               processors=[ResizeToFill(550, 355)],
                               format='JPEG',
                               options={'quality': 90})
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image_thumbnail = ImageSpecField(source='imageurl',  
                                      processors=[ResizeToFill(150, 150)],
                                      format='JPEG',
                                      options={'quality': 80})
       
    def __str__(self):
        return self.imageurl


class Categories(models.Model):
    name = models.CharField(max_length=255, blank=True)


class DigitialAssets(models.Model):
    token = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    imageMedia = models.ManyToManyField(PhotoMedia, blank=True)
    blochain = models.CharField(max_length=100)
    bid_price = models.CharField(max_length=100)
    category = models.OneToOneField(Categories, on_delete=models.CASCADE, related_name='category')
       
    def __str__(self):
        return self.title



