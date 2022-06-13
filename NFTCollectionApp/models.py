import jsonfield
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


class NFTCollection(models.Model):
    collection_id               = models.CharField(max_length=255, blank=True)
    collection_url              = models.CharField(max_length=255, blank=True)
    slug                        = models.CharField(max_length=255, blank=True)
    collection_type             = models.CharField(max_length=255, blank=True)
    collection_name             = models.CharField(max_length=255, blank=True)
    collection_description      = models.TextField(blank=True, default='')
    trades	                    = models.CharField(max_length=255, blank=True)
    volume                      = models.CharField(max_length=255, blank=True)
    floor                       = models.CharField(max_length=255, blank=True)
    collection_symbol           = models.CharField(max_length=255, blank=True)
    owner                       = models.CharField(max_length=255, blank=True)
    external_image_url          = models.CharField(max_length=255, blank=True)
    aws_bucket_image_url        = models.CharField(max_length=255, blank=True)
    external_link               = models.CharField(max_length=255, blank=True)
    buyer_fee_basis_points      = models.CharField(max_length=255, blank=True)
    seller_fee_basis_points     = models.CharField(max_length=255, blank=True)
    twitter_username            = models.CharField(max_length=255, blank=True)
    discord_url                 = models.CharField(max_length=255, blank=True)
    updated_at                  = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.collection_name

    class Meta:
        verbose_name = 'NFT Collection'
