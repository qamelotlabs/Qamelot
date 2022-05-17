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
from django import forms


class AssetsUsers(models.Model):
    user_type = models.CharField(max_length=254)
    username = models.CharField(max_length=254, blank=True)
    profile_img_url = models.CharField(max_length=254, blank=True)
    address = models.CharField(max_length=254)
    value = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.username
        
    class Meta:
        verbose_name = 'Assets User'


class AssetsImage(models.Model):
    type = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100)
    representation = models.CharField(max_length=100)
    mimeType = models.CharField(max_length=100)
    size = models.CharField(max_length=100, blank=True)
    width = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.url
        
    class Meta:
        verbose_name = 'Assets Image'


class APIPaginate(models.Model):
    total = models.CharField(max_length=100, blank=True)
    continuation = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
        
    class Meta:
        verbose_name = 'API Paginate'


class Assets(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    blockchain = models.CharField(max_length=100)
    collection = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    tokenId = models.CharField(max_length=100)
    owner_id = models.ForeignKey(
        AssetsUsers, on_delete=models.CASCADE, related_name='owner_id', blank=True
        )
    creator_id = models.ForeignKey(
        AssetsUsers, on_delete=models.CASCADE, related_name='creator_id', blank=True
        )
    mintedAt = models.CharField(max_length=100)
    lastUpdatedAt = models.CharField(max_length=100)
    supply = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, default='')
    image_id = models.ForeignKey(
        AssetsImage, on_delete=models.CASCADE, related_name='image_id', blank=True
        )
    permalink = models.CharField(max_length=100, blank=True)
    restriction = models.CharField(max_length=100, blank=True)
    deleted = models.BooleanField(default=False)
    auction = models.CharField(max_length=100, blank=True)
    totalStock = models.CharField(max_length=100, blank=True)
    sellers = models.IntegerField(default=0, blank=True)
    status = models.CharField(max_length=100, blank=True)
    platform = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Asset'
