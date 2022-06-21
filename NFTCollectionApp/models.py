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
    collectionAddress = models.CharField(max_length=255, blank=True)
    collectionUrl = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=255, blank=True)
    collectionType = models.CharField(max_length=255, blank=True)
    collectionName = models.CharField(max_length=255, blank=True)
    collectionDescription = models.TextField(blank=True, default='')
    collectionSymbol = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=255, blank=True)
    externalImageUrl = models.CharField(max_length=255, blank=True)
    awsBucketImageUrl = models.CharField(max_length=255, blank=True)
    externalLink = models.CharField(max_length=255, blank=True)
    safelistRequestStatus = models.CharField(max_length=255, blank=True)
    twitterUsername = models.CharField(max_length=255, blank=True)
    discordUrl = models.CharField(max_length=255, blank=True)
    createdAt = models.DateField(blank=True, null=True)
    updatedAt = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.collectionName

    class Meta:
        verbose_name = 'NFT Collection'


class collectionStat(models.Model):
    dateLog = models.DateField(blank=True, null=True)
    collectionId = models.ForeignKey(NFTCollection, on_delete=models.CASCADE, related_name='collectionId')
    oneDayVolume = models.CharField(max_length=255, blank=True)
    oneDayChange = models.CharField(max_length=255, blank=True)
    oneDaySales = models.CharField(max_length=255, blank=True)
    oneDayAveragePrice = models.CharField(max_length=255, blank=True)
    sevenDayVolume = models.CharField(max_length=255, blank=True)
    sevenDayChange = models.CharField(max_length=255, blank=True)
    sevenDaySales = models.CharField(max_length=255, blank=True)
    sevenDayAveragePrice = models.CharField(max_length=255, blank=True)
    thirtyDayVolume = models.CharField(max_length=255, blank=True)
    thirtyDayChange = models.CharField(max_length=255, blank=True)
    thirtyDaySales = models.CharField(max_length=255, blank=True)
    thirtyDayAveragePrice = models.CharField(max_length=255, blank=True)
    totalVolume = models.CharField(max_length=255, blank=True)
    totalSales = models.CharField(max_length=255, blank=True)
    totalSupply = models.CharField(max_length=255, blank=True)
    count = models.CharField(max_length=255, blank=True)
    numOwners = models.CharField(max_length=255, blank=True)
    averagePrice = models.CharField(max_length=255, blank=True)
    numReports = models.CharField(max_length=255, blank=True)
    marketCap = models.CharField(max_length=255, blank=True)
    floorPrice = models.CharField(max_length=255, blank=True)    
    
    def __str__(self):
        return self.totalVolume

    class Meta:
        verbose_name = 'Collection Stat'